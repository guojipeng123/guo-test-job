# coding=utf-8
"""
superuser command
"""
from django.core.cache import cache
from django.http import JsonResponse

from gcloud.core.decorators import check_is_superuser


@check_is_superuser()
def delete_cache_key(request, key):
    cache.delete(key)
    return JsonResponse({'result': True, 'data': 'success'})


@check_is_superuser()
def get_cache_key(request, key):
    data = cache.get(key)
    return JsonResponse({'result': True, 'data': data})
