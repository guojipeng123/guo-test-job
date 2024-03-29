# -*- coding: utf-8 -*-

import logging
import contextlib
import traceback

from pipeline.engine import states
from pipeline.engine.models import Status, NodeRelationship, FunctionSwitch
from pipeline.engine.core.handlers import FLOW_NODE_HANDLERS

logger = logging.getLogger('celery')


@contextlib.contextmanager
def runtime_exception_handler(process):
    try:
        yield
    except Exception as e:
        logger.error(traceback.format_exc(e))
        process.exit_gracefully(e)


def run_loop(process):
    """
    pipeline 推进主循环
    :param process: 当前进程
    :return:
    """
    with runtime_exception_handler(process):
        while True:
            current_node = process.top_pipeline.node(process.current_node_id)

            # check child process destination
            if process.destination_id == current_node.id:
                try:
                    process.destroy_and_wake_up_parent(current_node.id)
                except Exception as e:
                    logger.error(traceback.format_exc(e))
                logger.info('child process(%s) finish.' % process.id)
                return

            # check root pipeline status
            need_sleep, pipeline_state = process.root_sleep_check()
            if need_sleep:
                logger.info('pipeline(%s) turn to sleep.' % process.root_pipeline.id)
                process.sleep(do_not_save=(pipeline_state == states.REVOKED))
                return

            # check subprocess status
            need_sleep, subproc_above = process.subproc_sleep_check()
            if need_sleep:
                logger.info('process(%s) turn to sleep.' % process.root_pipeline.id)
                process.sleep(adjust_status=True, adjust_scope=subproc_above)
                return

            # check engine status
            if FunctionSwitch.objects.is_frozen():
                logger.info('pipeline(%s) have been frozen.' % process.id)
                process.freeze()
                return

            # try to transit current node to running state
            if not Status.objects.transit(id=current_node.id, to_state=states.RUNNING, start=True,
                                          name=str(current_node.__class__)).result:
                logger.info('can not transit node(%s) to running, pipeline(%s) turn to sleep.' % (
                    current_node.id, process.root_pipeline.id))
                process.sleep(adjust_status=True)
                return

            # refresh current node
            process.refresh_current_node(current_node.id)

            # build relationship
            NodeRelationship.objects.build_relationship(process.top_pipeline.id, current_node.id)
            result = FLOW_NODE_HANDLERS[current_node.__class__](process, current_node)

            if result.should_return or result.should_sleep:
                if result.should_sleep:
                    process.sleep(adjust_status=True)
                return

            # store current node id
            process.current_node_id = result.next_node.id
