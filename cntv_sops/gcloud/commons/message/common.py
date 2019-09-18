# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _


def title_and_content_for_atom_failed(taskflow, pipeline_inst, atom_node_name, executor):
    title = _(u"【标准运维APP通知】执行失败")
    content = _(u"您在【{cc_name}】业务中的任务【{task_name}】执行失败，当前失败节点是【{node_name}】，"
                u"操作员是【{executor}】，请前往标准运维APP( {url} )查看详情！").format(
        cc_name=taskflow.business.cc_name,
        task_name=pipeline_inst.name,
        node_name=atom_node_name,
        executor=executor,
        url=taskflow.url
    )
    return title, content


def title_and_content_for_flow_finished(taskflow, pipeline_inst, atom_node_name, executor):
    title = _(u"【标准运维APP通知】执行完成")
    content = _(u"您在【{cc_name}】业务中的任务【{task_name}】执行成功，操作员是【{executor}】，"
                u"请前往标准运维APP( {url} )查看详情！").format(
        cc_name=taskflow.business.cc_name,
        task_name=pipeline_inst.name,
        executor=executor,
        url=taskflow.url
    )
    return title, content


def title_and_content_for_periodic_task_start_fail(template, periodic_task, history):
    title = _(u"【标准运维APP通知】周期任务启动失败")
    content = _(u"您在【{cc_name}】业务中计划于【{start_time}】执行的周期任务【{task_name}】启动失败，"
                u"错误信息：【{ex_data}】").format(
        cc_name=template.business.cc_name,
        start_time=history.start_at,
        task_name=periodic_task.name,
        ex_data=history.ex_data
    )
    return title, content
