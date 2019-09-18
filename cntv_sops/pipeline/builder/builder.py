# -*- coding: utf-8 -*-
import copy
import Queue

from pipeline.utils.uniqid import uniqid
from pipeline.core.constants import PE

__all__ = [
    'build_tree'
]

__skeleton = {
    PE.id: None,
    PE.start_event: None,
    PE.end_event: None,
    PE.activities: {},
    PE.gateways: {},
    PE.flows: {},
    PE.data: {
        PE.inputs: {},
        PE.outputs: {}
    }
}

__node_type = {
    PE.ServiceActivity: PE.activities,
    PE.SubProcess: PE.activities,
    PE.EmptyEndEvent: PE.end_event,
    PE.EmptyStartEvent: PE.start_event,
    PE.ParallelGateway: PE.gateways,
    PE.ExclusiveGateway: PE.gateways,
    PE.ConvergeGateway: PE.gateways
}

__start_elem = {
    PE.EmptyStartEvent
}

__end_elem = {
    PE.EmptyEndEvent
}

__multiple_incoming_type = {
    PE.ServiceActivity,
    PE.ConvergeGateway,
    PE.EmptyEndEvent
}

__incoming = '__incoming'


def build_tree(start_elem, id=None, data=None):
    tree = copy.deepcopy(__skeleton)
    elem_queue = Queue.Queue()
    processed_elem = set()

    tree[__incoming] = {}
    elem_queue.put(start_elem)

    while not elem_queue.empty():
        # get elem
        elem = elem_queue.get()

        # update node when we meet again
        if elem.id in processed_elem:
            __update(tree, elem)
            continue

        # add to queue
        for e in elem.outgoing:
            elem_queue.put(e)

        # mark as processed
        processed_elem.add(elem.id)

        # tree grow
        __grow(tree, elem)

    del tree[__incoming]
    tree[PE.id] = id or uniqid()
    tree[PE.data] = data or tree[PE.data]
    return tree


def __update(tree, elem):
    tree[__node_type[elem.type()]][elem.id][PE.incoming] = tree[__incoming][elem.id]


def __grow(tree, elem):
    if elem.type() in __start_elem:
        outgoing = uniqid()
        tree[PE.start_event] = {
            PE.incoming: '',
            PE.outgoing: outgoing,
            PE.type: elem.type(),
            PE.id: elem.id,
            PE.name: elem.name
        }

        next_elem = elem.outgoing[0]
        __grow_flow(tree, outgoing, elem, next_elem)

    elif elem.type() in __end_elem:
        tree[PE.end_event] = {
            PE.incoming: tree[__incoming][elem.id],
            PE.outgoing: '',
            PE.type: elem.type(),
            PE.id: elem.id,
            PE.name: elem.name
        }

    elif elem.type() == PE.ServiceActivity:
        outgoing = uniqid()

        tree[PE.activities][elem.id] = {
            PE.incoming: tree[__incoming][elem.id],
            PE.outgoing: outgoing,
            PE.type: elem.type(),
            PE.id: elem.id,
            PE.name: elem.name,
            PE.error_ignorable: False,
            PE.component: elem.component_dict(),
            PE.optional: False
        }

        next_elem = elem.outgoing[0]
        __grow_flow(tree, outgoing, elem, next_elem)

    elif elem.type() == PE.SubProcess:
        outgoing = uniqid()

        tree[PE.activities][elem.id] = {
            PE.id: elem.id,
            PE.incoming: tree[__incoming][elem.id],
            PE.name: elem.name,
            PE.outgoing: outgoing,
            PE.type: elem.type(),
            PE.pipeline: build_tree(
                start_elem=elem.start,
                id=elem.id,
                data=elem.data
            ),
            PE.params: elem.params
        }

        next_elem = elem.outgoing[0]
        __grow_flow(tree, outgoing, elem, next_elem)

    elif elem.type() == PE.ParallelGateway:
        outgoing = [uniqid() for _ in xrange(len(elem.outgoing))]

        tree[PE.gateways][elem.id] = {
            PE.id: elem.id,
            PE.incoming: tree[__incoming][elem.id],
            PE.outgoing: outgoing,
            PE.type: elem.type(),
            PE.name: elem.name
        }

        for i, next_elem in enumerate(elem.outgoing):
            __grow_flow(tree, outgoing[i], elem, next_elem)

    elif elem.type() == PE.ExclusiveGateway:
        outgoing = [uniqid() for _ in xrange(len(elem.outgoing))]

        tree[PE.gateways][elem.id] = {
            PE.id: elem.id,
            PE.incoming: tree[__incoming][elem.id],
            PE.outgoing: outgoing,
            PE.type: elem.type(),
            PE.name: elem.name,
            PE.conditions: elem.link_conditions_with(outgoing)
        }

        for i, next_elem in enumerate(elem.outgoing):
            __grow_flow(tree, outgoing[i], elem, next_elem)

    elif elem.type() == PE.ConvergeGateway:
        outgoing = uniqid()

        tree[PE.gateways][elem.id] = {
            PE.id: elem.id,
            PE.incoming: tree[__incoming][elem.id],
            PE.outgoing: outgoing,
            PE.type: elem.type(),
            PE.name: elem.name
        }

        next_elem = elem.outgoing[0]
        __grow_flow(tree, outgoing, elem, next_elem)

    else:
        raise Exception()


def __grow_flow(tree, outgoing, elem, next_element):
    tree[PE.flows][outgoing] = {
        PE.is_default: False,
        PE.source: elem.id,
        PE.target: next_element.id,
        PE.id: outgoing
    }
    if next_element.type() in __multiple_incoming_type:
        tree[__incoming].setdefault(next_element.id, []).append(outgoing)
    else:
        tree[__incoming][next_element.id] = outgoing
