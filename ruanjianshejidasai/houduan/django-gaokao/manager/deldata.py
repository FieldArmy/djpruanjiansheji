from django.http import JsonResponse
from common.models import Students, Teachers
import json


def del_data(request):
    # 身份校验
    '''if request.seession.get('mng'):
        if request.seession['mng'] != 'qwe43rrt':
            return JsonResponse({'ret': 1, 'msg': '权限不足'})
    else:
        return JsonResponse({'ret': 1, 'msg': '权限不足'})'''
    if request.method != 'DELETE':
        return JsonResponse({'ret': 1, 'msg': '不存在该请求'})
    request_params = json.loads(request.body)
    if request_params['action'] == 'del_user':
        try:
            # 从表中找到相应的记录
            data = Students.objects.get(account=request_params['account_user'])
            data.delete()
        except:
            return JsonResponse({'ret': 1, 'msg': '无法删除'})
        return JsonResponse({'ret': 0})
    elif request_params['action'] == 'del_teacher':
        try:
            # 从表中找到相应的记录
            data = Teachers.objects.get(account=request_params['account_teacher'])
            data.delete()
        except:
            return JsonResponse({'ret': 1, 'msg': '无法删除'})
        return JsonResponse({'ret': 0})