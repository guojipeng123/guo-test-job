# -*- coding: utf-8 -*-
from ..base import ComponentAPI


class CollectionsBkPaas(object):
    """Collections of BK_PAAS APIS"""

    def __init__(self, client):
        self.client = client

        self.get_app_info = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/bk_paas/get_app_info/',
            description=u'获取应用信息'
        )
        self.create_app = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/bk_paas/create_app/',
            description=u'创建一个轻应用'
        )
        self.edit_app = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/bk_paas/edit_app/',
            description=u'编辑一个轻应用'
        )
        self.del_app = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/bk_paas/del_app/',
            description=u'下架一个轻应用'
        )
        self.modify_app_logo = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/bk_paas/modify_app_logo/',
            description=u'修改轻应用的 logo'
        )
