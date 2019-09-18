# -*- coding: utf-8 -*-
"""
# 作业平台任务状态参照表
TASK_RESULT = [
    (0, u'状态未知'),
    (1, u'未执行'),
    (2, u'正在执行'),
    (3, u'执行成功'),
    (4, u'执行失败'),
    (5, u'跳过'),
    (6, u'忽略错误'),
    (7, u'等待用户'),
    (8, u'手动结束'),
    (9, u'状态异常'),
    (10, u'步骤强制终止中'),
    (11, u'步骤强制终止成功'),
    (12, u'步骤强制终止失败'),
    (-1, u'接口调用失败'),
]
"""
import base64
from urllib import urlencode

from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from blueapps.utils.esbclient import get_client_by_user

from pipeline.conf import settings
from pipeline_plugins.components.utils import cc_get_ips_info_by_str
from pipeline.core.flow.activity import Service, StaticIntervalGenerator
from pipeline.component_framework.component import Component

JOB_SUCCESS = [3, 11]
JOB_APP_CODE = 'bk_job'
__group_name__ = _(u"作业平台(JOB)")
__group_icon__ = '%scomponents/icons/job.png' % settings.STATIC_URL


class JobService(Service):
    __need_schedule__ = True
    interval = StaticIntervalGenerator(5)

    @staticmethod
    def set_outputs_job_url(data, parent_data):
        job_inst_id = data.outputs.job_inst_id
        client = data.outputs.client
        client.set_bk_api_ver("v2")
        query = {
            'app': JOB_APP_CODE,
            'url': u'%s?taskInstanceList&appId=%s#taskInstanceId=%s' % (
                settings.BK_JOB_HOST,
                parent_data.inputs.biz_cc_id,
                job_inst_id,
            )
        }
        job_inst_url = "%s/console/?%s" % (settings.BK_URL, urlencode(query))
        data.outputs.job_inst_url = job_inst_url

    def execute(self, data, parent_data):
        pass

    def schedule(self, data, parent_data, callback_data=None):
        if parent_data.get_one_of_inputs('language'):
            translation.activate(parent_data.get_one_of_inputs('language'))

        job_inst_id = data.outputs.job_inst_id
        client = data.outputs.client
        job_kwargs = {
            'bk_biz_id': parent_data.get_one_of_inputs('biz_cc_id'),
            'job_instance_id': job_inst_id,
        }
        job_result = client.job.get_job_instance_status(job_kwargs)
        if not job_result['result']:
            data.set_outputs('ex_data', job_result['message'])
            self.finish_schedule()
            return False
        # 任务执行结束
        job_data = job_result['data']
        if job_data['is_finished']:
            # 执行成功
            if job_data['job_instance'].get('status', 0) in JOB_SUCCESS:
                # 全局变量重载
                global_var_result = client.job.get_job_instance_global_var_value({
                    "bk_biz_id": parent_data.get_one_of_inputs('biz_cc_id'),
                    "job_instance_id": job_inst_id
                })

                if not global_var_result['result']:
                    data.set_outputs('ex_data', global_var_result['message'])
                    self.finish_schedule()
                    return False

                global_var_list = global_var_result['data'].get('job_instance_var_values', [])
                if global_var_list:
                    for global_var in global_var_list[-1]['step_instance_var_values']:
                        # 2为ip类型不设置
                        if global_var['category'] != 2:
                            data.set_outputs(global_var['name'], global_var['value'])

                data.set_outputs('data', job_data)
                self.finish_schedule()
                return True
            # 执行失败
            else:
                data.set_outputs('ex_data', _(u"任务执行失败，<a href='%s' target='_blank'>"
                                              u"前往作业平台(JOB)查看详情</a>") % data.outputs.job_inst_url,
                                 )
                self.finish_schedule()
                return False

        return True

    def outputs_format(self):
        return [
            self.OutputItem(name=_(u'JOB任务ID'), key='job_inst_id', type='int'),
            self.OutputItem(name=_(u'JOB任务链接'), key='job_inst_url', type='str')
        ]


class JobExecuteTaskService(JobService):
    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        client = get_client_by_user(executor)
        client.set_bk_api_ver("v2")
        if parent_data.get_one_of_inputs('language'):
            setattr(client, 'language', parent_data.get_one_of_inputs('language'))
            translation.activate(parent_data.get_one_of_inputs('language'))

        original_global_var = data.get_one_of_inputs('job_global_var')
        global_vars = []
        for _value in original_global_var:
            # 1-字符串，2-IP
            if _value['type'] == 2:
                var_ip = cc_get_ips_info_by_str(
                    executor,
                    biz_cc_id,
                    _value['value'])
                ip_list = [{'ip': _ip['InnerIP'], 'bk_cloud_id': _ip['Source']} for _ip in var_ip['ip_result']]
                global_vars.append({
                    'id': _value['id'],
                    'ip_list': ip_list,
                })
            else:
                global_vars.append({
                    'id': _value['id'],
                    'value': _value['value'].strip(),
                })

        job_kwargs = {
            'bk_biz_id': biz_cc_id,
            'bk_job_id': data.get_one_of_inputs('job_task_id'),
            'global_vars': global_vars,
        }

        job_result = client.job.execute_job(job_kwargs)
        if job_result['result']:
            data.set_outputs('job_inst_id', job_result['data']['job_instance_id'])
            data.set_outputs('job_inst_name', job_result['data']['job_instance_name'])
            data.set_outputs('client', client)
            self.set_outputs_job_url(data, parent_data)
            return True
        else:
            data.set_outputs('ex_data', job_result['message'])
            return False

    def schedule(self, data, parent_data, callback_data=None):
        return super(JobExecuteTaskService, self).schedule(data, parent_data, callback_data)

    def outputs_format(self):
        return super(JobExecuteTaskService, self).outputs_format()


class JobExecuteTaskComponent(Component):
    name = _(u'执行作业')
    code = 'job_execute_task'
    bound_service = JobExecuteTaskService
    form = '%scomponents/atoms/sites/%s/job/job_execute_task.js' % (settings.STATIC_URL, settings.RUN_VER)


class JobFastPushFileService(JobService):
    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        client = get_client_by_user(executor)
        client.set_bk_api_ver("v2")
        if parent_data.get_one_of_inputs('language'):
            setattr(client, 'language', parent_data.get_one_of_inputs('language'))
            translation.activate(parent_data.get_one_of_inputs('language'))

        original_source_files = data.get_one_of_inputs('job_source_files', [])
        file_source = []
        for item in original_source_files:
            ip_info = cc_get_ips_info_by_str(executor, biz_cc_id, item['ip'])
            file_source.append({
                'files': item['files'].strip().split("\n"),
                'ip_list': [{
                    'ip': _ip['InnerIP'],
                    'bk_cloud_id': _ip['Source']
                } for _ip in ip_info['ip_result']],
                'account': item['account'].strip(),
            })

        original_ip_list = data.get_one_of_inputs('job_ip_list')
        ip_info = cc_get_ips_info_by_str(executor, biz_cc_id, original_ip_list)
        ip_list = [{'ip': _ip['InnerIP'], 'bk_cloud_id': _ip['Source']}
                   for _ip in ip_info['ip_result']]

        job_kwargs = {
            'bk_biz_id': biz_cc_id,
            'file_source': file_source,
            'ip_list': ip_list,
            'account': data.get_one_of_inputs('job_account'),
            'file_target_path': data.get_one_of_inputs('job_target_path'),
        }

        job_result = client.job.fast_push_file(job_kwargs)
        if job_result['result']:
            data.set_outputs('job_inst_id', job_result['data']['job_instance_id'])
            data.set_outputs('job_inst_name', job_result['data']['job_instance_name'])
            data.set_outputs('client', client)
            self.set_outputs_job_url(data, parent_data)
            return True
        else:
            data.set_outputs('ex_data', job_result['message'])
            return False

    def schedule(self, data, parent_data, callback_data=None):
        return super(JobFastPushFileService, self).schedule(data, parent_data, callback_data)

    def outputs_format(self):
        return super(JobFastPushFileService, self).outputs_format()


class JobFastPushFileComponent(Component):
    name = _(u'快速分发文件')
    code = 'job_fast_push_file'
    bound_service = JobFastPushFileService
    form = '%scomponents/atoms/job/job_fast_push_file.js' % settings.STATIC_URL


class JobFastExecuteScriptService(JobService):
    def execute(self, data, parent_data):
        executor = parent_data.get_one_of_inputs('executor')
        biz_cc_id = parent_data.get_one_of_inputs('biz_cc_id')
        client = get_client_by_user(executor)
        client.set_bk_api_ver("v2")
        if parent_data.get_one_of_inputs('language'):
            setattr(client, 'language', parent_data.get_one_of_inputs('language'))
            translation.activate(parent_data.get_one_of_inputs('language'))

        original_ip_list = data.get_one_of_inputs('job_ip_list')
        ip_info = cc_get_ips_info_by_str(executor, biz_cc_id, original_ip_list)
        ip_list = [{'ip': _ip['InnerIP'], 'bk_cloud_id': _ip['Source']}
                   for _ip in ip_info['ip_result']]

        job_kwargs = {
            'bk_biz_id': biz_cc_id,
            'script_timeout': data.get_one_of_inputs('job_script_timeout'),
            'account': data.get_one_of_inputs('job_account'),
            'ip_list': ip_list,
        }

        script_param = data.get_one_of_inputs('job_script_param')
        if script_param:
            job_kwargs.update({
                'script_param': base64.b64encode(script_param.encode('utf-8'))
            })

        script_source = data.get_one_of_inputs('job_script_source')
        if script_source in ["general", "public"]:
            job_kwargs.update({
                "script_id": data.get_one_of_inputs('job_script_list_%s' % script_source)
            })
        else:
            job_kwargs.update({
                'script_type': data.get_one_of_inputs('job_script_type'),
                'script_content': base64.b64encode(data.get_one_of_inputs('job_content').encode('utf-8')),
            })

        job_result = client.job.fast_execute_script(job_kwargs)
        if job_result['result']:
            data.set_outputs('job_inst_id', job_result['data']['job_instance_id'])
            data.set_outputs('job_inst_name', job_result['data']['job_instance_name'])
            data.set_outputs('client', client)
            self.set_outputs_job_url(data, parent_data)
            return True
        else:
            data.set_outputs('ex_data', '%s, invalid ip: %s' % (job_result['message'], ','.join(ip_info['invalid_ip'])))
            return False

    def schedule(self, data, parent_data, callback_data=None):
        return super(JobFastExecuteScriptService, self).schedule(data, parent_data, callback_data)

    def outputs_format(self):
        return super(JobFastExecuteScriptService, self).outputs_format()


class JobFastExecuteScriptComponent(Component):
    name = _(u'快速执行脚本')
    code = 'job_fast_execute_script'
    bound_service = JobFastExecuteScriptService
    form = '%scomponents/atoms/job/job_fast_execute_script.js' % settings.STATIC_URL
