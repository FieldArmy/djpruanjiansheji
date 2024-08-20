from django.http import JsonResponse
from common.models import Teachers
import json


def personal_data(request):
    '''if request.seession.get('tch'):
        if request.seession['tch'] != 'ww33ert':
            return JsonResponse({'ret': 1, 'msg': '权限不足'})
    else:
        return JsonResponse({'ret': 1, 'msg': '权限不足'})'''
    request_params = json.loads(request)
    if request_params['action'] == 'get_teachers':
        try:
            teacher = Teachers.objects.get(account=request_params['account'])
        except:
            return JsonResponse({'ret': 1, 'msg': '未查询到相关信息'})
        data = {
            'name': teacher.name,
            'sex': teacher.sex,
            'mail': teacher.mail,
            'phonenumber': teacher.phonenumber,
            'age': teacher.age,
            'major': teacher.major_type,
            'major_set': teacher.major_set
        }
        return JsonResponse({'ret': 0, 'data': data})
    elif request_params['action'] == 'set_teachers':
        try:
            teacher = Teachers.objects.get(account=request_params['account'])
        except:
            return JsonResponse({'ret': 1, 'msg': '未查询到相关信息'})
        teacher.name = request_params['name']
        teacher.mail = request_params['mail']
        teacher.age = request_params['age']
        teacher.phonenumber = request_params['phonenumber']
        teacher.major_type = request_params['major']
        teacher.sex = request_params['sex']
        teacher.save()
        return JsonResponse({'ret': 0})
