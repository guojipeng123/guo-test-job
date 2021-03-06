# -*- coding: utf-8 -*-


class PipelineElement(object):
    ServiceActivity = 'ServiceActivity'
    LoopServiceActivity = 'LoopServiceActivity'
    SubProcess = 'SubProcess'
    ExclusiveGateway = 'ExclusiveGateway'
    ParallelGateway = 'ParallelGateway'
    ConvergeGateway = 'ConvergeGateway'
    EmptyStartEvent = 'EmptyStartEvent'
    EmptyEndEvent = 'EmptyEndEvent'

    pipeline = 'pipeline'
    id = 'id'
    type = 'type'
    start_event = 'start_event'
    end_event = 'end_event'
    activities = 'activities'
    flows = 'flows'
    gateways = 'gateways'
    constants = 'constants'
    conditions = 'conditions'
    incoming = 'incoming'
    outgoing = 'outgoing'
    source = 'source'
    target = 'target'
    data = 'data'
    component = 'component'
    evaluate = 'evaluate'
    name = 'name'
    inputs = 'inputs'
    outputs = 'outputs'
    source_act = 'source_act'
    source_key = 'source_key'
    code = 'code'
    error_ignorable = 'error_ignorable'
    skippable = 'skippable'
    can_retry = 'can_retry'
    timeout = 'timeout'
    loop_times = 'loop_times'
    converge_gateway_id = 'converge_gateway_id'
    is_param = 'is_param'
    value = 'value'
    params = 'params'
    is_default = 'is_default'
    optional = 'optional'
    template_id = 'template_id'
    plain = 'plain'
    splice = 'splice'
    lazy = 'lazy'

    location = 'location'
    line = 'line'


PE = PipelineElement()
