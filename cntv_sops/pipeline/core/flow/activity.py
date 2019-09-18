# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from copy import copy

from django.utils.translation import ugettext_lazy as _

from pipeline.core.flow.base import FlowNode
from collections import namedtuple


def _empty_method(data, parent_data):
    return


class Activity(FlowNode):
    __metaclass__ = ABCMeta

    def __init__(self, id, name=None, data=None, failure_handler=None):
        super(Activity, self).__init__(id, name, data)
        self._failure_handler = failure_handler or _empty_method

    def next(self):
        return self.outgoing.unique_one().target

    def failure_handler(self, parent_data):
        return self._failure_handler(data=self.data, parent_data=parent_data)

    def skip(self):
        raise NotImplementedError()


class ServiceActivity(Activity):
    result_bit = '_result'

    def __init__(self, id, service, name=None, data=None, error_ignorable=False, failure_handler=None, skippable=True,
                 can_retry=True, timeout=None):
        super(ServiceActivity, self).__init__(id, name, data, failure_handler)
        self.service = service
        self.error_ignorable = error_ignorable
        self._prepared_inputs = self.data.inputs_copy()
        self._prepared_outputs = self.data.outputs_copy()
        self.skippable = skippable
        self.can_retry = can_retry
        self.timeout = timeout

    def execute(self, parent_data):
        self.service.logger = self.logger
        self.service.id = self.id
        result = self.service.execute(self.data, parent_data)

        # set result
        self.set_result_bit(result)

        if self.error_ignorable:
            return True
        return result

    def set_result_bit(self, result):
        self.data.set_outputs(self.result_bit, bool(result))

    def get_result_bit(self):
        return self.data.get_one_of_outputs(self.result_bit)

    def skip(self):
        self.set_result_bit(True)
        return True

    def ignore_error(self):
        self.set_result_bit(False)
        return True

    def clear_outputs(self):
        self.data.reset_outputs({})

    def need_schedule(self):
        return self.service.need_schedule()

    def schedule(self, parent_data, callback_data=None):
        self.service.logger = self.logger
        self.service.id = self.id
        result = self.service.schedule(self.data, parent_data, callback_data)
        self.set_result_bit(result)

        if result is False:
            if self.error_ignorable:
                self.service.finish_schedule()
                return True

        return result

    def is_schedule_done(self):
        return self.service.is_schedule_finished()

    def finish_schedule(self):
        self.service.finish_schedule()

    def shell(self):
        shell = ServiceActivity(id=self.id, service=self.service, name=self.name, data=self.data,
                                error_ignorable=self.error_ignorable, timeout=self.timeout)
        return shell

    def schedule_fail(self):
        return

    def schedule_success(self):
        return

    def prepare_rerun_data(self):
        self.data.override_inputs(copy(self._prepared_inputs))
        self.data.override_outputs(copy(self._prepared_outputs))


class LoopServiceActivity(ServiceActivity):

    def __init__(self, loop_times, *args, **kwargs):
        super(LoopServiceActivity, self).__init__(*args, **kwargs)
        self.loop_times = loop_times
        self.current_loop = 0
        self.actual_loop = 0

    def execute(self, parent_data):

        # clean status
        if self.current_loop != 0:
            self.service.clean_status()

        self.service.logger = self.logger
        result = self.service.execute(self.data, parent_data)

        # set result
        self.set_result_bit(result)

        if not result and self.error_ignorable:
            return True

        return result

    def schedule(self, parent_data, callback_data=None):
        self.service.logger = self.logger
        result = self.service.schedule(self.data, parent_data, callback_data)

        self.set_result_bit(result)

        if not result and self.error_ignorable:
            self.service.finish_schedule()
            return True

        return result

    def skip(self):
        self.current_loop = self.loop_times
        return super(LoopServiceActivity, self).skip()

    def ignore_error(self):
        self.current_loop = self.loop_times
        return super(LoopServiceActivity, self).ignore_error()

    def revert_ignore_error(self):
        self.current_loop = self.actual_loop

    def next(self):
        if self.current_loop < self.loop_times:
            return self
        return super(LoopServiceActivity, self).next()

    def loop_success(self):
        self.actual_loop += 1
        self.current_loop += 1

    def shell(self):
        shell = LoopServiceActivity(id=self.id, service=self.service, name=self.name, data=self.data,
                                    error_ignorable=self.error_ignorable, loop_times=self.loop_times)
        shell.loop_times = self.loop_times
        shell.actual_loop = self.actual_loop
        shell.current_loop = self.current_loop
        return shell

    def prepare_loop_data(self):
        if self.current_loop != 0:
            self.data.override_inputs(copy(self._prepared_inputs))
            self.data.override_outputs(copy(self._prepared_outputs))

    def schedule_fail(self):
        pass

    def schedule_success(self):
        pass


class SubProcess(Activity):
    def __init__(self, id, pipeline, name=None):
        super(SubProcess, self).__init__(id, name, pipeline.data)
        self.pipeline = pipeline


class Service(object):
    __metaclass__ = ABCMeta

    ScheduleResultAttr = '__schedule_finish__'
    ScheduleDetermineAttr = '__need_schedule__'
    OutputItem = namedtuple('OutputItem', 'name key type')
    interval = None
    _result_output = OutputItem(name=_(u'执行结果'), key='_result', type='bool')

    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def execute(self, data, parent_data):
        # get params from data
        pass

    @abstractmethod
    def outputs_format(self):
        pass

    def outputs(self):
        custom_format = self.outputs_format()
        assert isinstance(custom_format, list)
        custom_format.append(self._result_output)
        return custom_format

    def need_schedule(self):
        return getattr(self, Service.ScheduleDetermineAttr, False)

    def schedule(self, data, parent_data, callback_data=None):
        return True

    def finish_schedule(self):
        setattr(self, self.ScheduleResultAttr, True)

    def is_schedule_finished(self):
        return getattr(self, self.ScheduleResultAttr, False)

    def __getstate__(self):
        if 'logger' in self.__dict__:
            del self.__dict__['logger']
        return self.__dict__

    def clean_status(self):
        setattr(self, self.ScheduleResultAttr, False)


class AbstractIntervalGenerator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.count = 0

    def next(self):
        self.count += 1


class DefaultIntervalGenerator(AbstractIntervalGenerator):
    def next(self):
        super(DefaultIntervalGenerator, self).next()
        return self.count ** 2


class NullIntervalGenerator(AbstractIntervalGenerator):
    pass


class StaticIntervalGenerator(AbstractIntervalGenerator):
    def __init__(self, interval):
        super(StaticIntervalGenerator, self).__init__()
        self.interval = interval

    def next(self):
        super(StaticIntervalGenerator, self).next()
        return self.interval
