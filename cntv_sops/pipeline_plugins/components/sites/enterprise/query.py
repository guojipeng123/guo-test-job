# -*- coding: utf-8 -*-
import importlib
import logging

from django.http import JsonResponse

from blueapps.utils.esbclient import get_client_by_request
from pipeline.conf import settings
from pipeline_plugins.components.utils import cc_get_inner_ip_by_module_id

atoms_cc = importlib.import_module('pipeline_plugins.components.collections.sites.%s.cc' % settings.RUN_VER)
logger = logging.getLogger('root')


def cc_search_object_attribute(request, obj_id, biz_cc_id):
    """
    @summary: 获取对象自定义属性
    @param request:
    @param biz_cc_id:
    @return:
    """
    client = get_client_by_request(request)
    client.set_bk_api_ver('v2')
    kwargs = {
        'bk_obj_id': obj_id,
    }
    cc_result = client.cc.search_object_attribute(kwargs)
    if not cc_result['result']:
        message = atoms_cc.cc_handle_api_error('cc.search_object_attribute', kwargs, cc_result['message'])
        logger.error(message)
        result = {
            'result': False,
            'data': [],
            'message': message
        }
        return JsonResponse(result)

    obj_property = []
    for item in cc_result['data']:
        if item['editable']:
            obj_property.append({
                'value': item['bk_property_id'],
                'text': item['bk_property_name']
            })

    return JsonResponse({'result': True, 'data': obj_property})


def cc_search_create_object_attribute(request, obj_id, biz_cc_id):
    client = get_client_by_request(request)
    client.set_bk_api_ver('v2')
    kwargs = {
        'bk_obj_id': obj_id,
    }
    cc_result = client.cc.search_object_attribute(kwargs)
    if not cc_result['result']:
        message = atoms_cc.cc_handle_api_error('cc.search_object_attribute', kwargs, cc_result['message'])
        logger.error(message)
        result = {
            'result': False,
            'data': [],
            'message': message
        }
        return JsonResponse(result)

    obj_property = []
    for item in cc_result['data']:
        if item['editable']:
            prop_dict = {
                'tag_code': item['bk_property_id'],
                'type': "input",
                'attrs': {
                    'name': item['bk_property_name'],
                    'editable': 'true',
                },
            }
            if item['bk_property_id'] in ['bk_set_name']:
                prop_dict["attrs"]["validation"] = [
                    {
                        "type": "required"
                    }
                ]
            obj_property.append(prop_dict)

    return JsonResponse({'result': True, 'data': obj_property})


def cc_format_topo_data(data, obj_id, category):
    """
    @summary: 格式化拓扑数据
    @param obj_id set\module
    @param category prev(获取obj_id上一层级拓扑)\ normal (获取obj_id层级拓扑) \picker(ip选择器拓扑)
    @return 拓扑数据列表
    """
    tree_data = []
    for item in data:
        tree_item = {
            'id': "%s_%s" % (item['bk_obj_id'], item['bk_inst_id']),
            'label': item['bk_inst_name']
        }
        if category == "prev":
            if item['bk_obj_id'] != obj_id:
                tree_data.append(tree_item)
                if item.get('child'):
                    tree_item['children'] = cc_format_topo_data(item['child'], obj_id, category)
        else:
            if item['bk_obj_id'] == obj_id:
                tree_data.append(tree_item)
            elif item.get('child'):
                tree_item['children'] = cc_format_topo_data(item['child'], obj_id, category)
                tree_data.append(tree_item)

    return tree_data


def cc_format_module_hosts(username, biz_cc_id, module_id_list):
    module_host_list = cc_get_inner_ip_by_module_id(username, biz_cc_id, module_id_list)
    module_host_dict = {}
    for item in module_host_list:
        for module in item['module']:
            if module_host_dict.get('module_%s' % module['bk_module_id']):
                module_host_dict['module_%s' % module['bk_module_id']].append({
                    'id': '%s_%s' % (module['bk_module_id'], item['host']['bk_host_innerip']),
                    'label': item['host']['bk_host_innerip']
                })
            else:
                module_host_dict['module_%s' % module['bk_module_id']] = [{
                    'id': '%s_%s' % (module['bk_module_id'], item['host']['bk_host_innerip']),
                    'label': item['host']['bk_host_innerip']
                }]
    return module_host_dict


def cc_search_topo(request, obj_id, category, biz_cc_id):
    """
    @summary: 查询对象拓扑
    @param request:
    @param biz_cc_id:
    @return:
    """
    client = get_client_by_request(request)
    client.set_bk_api_ver('v2')
    kwargs = {
        'bk_biz_id': biz_cc_id
    }
    cc_result = client.cc.search_biz_inst_topo(kwargs)
    if not cc_result['result']:
        message = atoms_cc.cc_handle_api_error('cc.search_biz_inst_topo', kwargs, cc_result['message'])
        logger.error(message)
        result = {
            'result': False,
            'data': [],
            'message': message
        }
        return JsonResponse(result)

    if category in ["normal", "prev", "picker"]:
        cc_topo = cc_format_topo_data(cc_result['data'], obj_id, category)
    else:
        cc_topo = []

    return JsonResponse({'result': True, 'data': cc_topo})


def cc_get_host_by_module_id(request, biz_cc_id):
    """
    查询模块对应主机
    :param request:
    :param biz_cc_id:
    :return:
    """
    select_module_id = request.GET.getlist('query', [])
    # 查询module对应的主机
    module_hosts = cc_format_module_hosts(request.user.username, biz_cc_id, map(lambda x: int(x), select_module_id))

    for del_id in (set(module_hosts.keys()) - set(map(lambda x: 'module_%s' % x, select_module_id))):
        del module_hosts[del_id]

    return JsonResponse({'result': True if module_hosts else False, 'data': module_hosts})


def job_get_script_list(request, biz_cc_id):
    """
    查询业务脚本列表
    :param request:
    :param biz_cc_id:
    :return:
    """
    # 查询脚本列表
    client = get_client_by_request(request)
    client.set_bk_api_ver('v2')
    script_type = request.GET.get('type')
    kwargs = {
        'bk_biz_id': biz_cc_id,
        'is_public': True if script_type == 'public' else False
    }
    script_result = client.job.get_script_list(kwargs)

    if not script_result['result']:
        message = atoms_cc.cc_handle_api_error('job.get_script_list', kwargs, script_result['message'])
        logger.error(message)
        result = {
            'result': False,
            'message': message
        }
        return JsonResponse(result)

    script_dict = {}
    for script in script_result['data']['data']:
        script_dict.setdefault(script['name'], []).append(script['id'])

    version_data = []
    for name, version in script_dict.items():
        version_data.append({
            "text": name,
            "value": max(version)
        })

    return JsonResponse({'result': True, 'data': version_data})
