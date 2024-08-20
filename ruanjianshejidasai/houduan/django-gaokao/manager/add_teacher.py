from django.http import JsonResponse
from common.models import Students, Teachers
import json


# 添加咨询师信息
def add_teacher(request):
    # 身份校验
    '''if request.seession.get('mng'):
        if request.seession['mng'] != 'qwe43rrt':
            return JsonResponse({'ret': 1, 'msg': '权限不足'})
    else:
        return JsonResponse({'ret': 1, 'msg': '权限不足'})'''
    request_params = json.loads(request.body)
    try:
        Teachers.objects.create(
            major_set=request_params['major_set'],
            # 专业门类
            major_type=request_params['major'],
            # 姓名
            name=request_params['name'],
            # 性别
            sex=request_params['sex'],
            # 年龄
            age=request_params['age'],
            # 账户
            account=request_params['tch_account'],
            # 密码
            password=request_params['tch_password'],
            # 个人简介
            text=request_params['text'],
            # 联系电话
            phonenumber=request_params['phonenumber'],
            # 联系邮箱
            mail=request_params['mail'],
        )
        return JsonResponse({'ret': 0})
    except:
        return JsonResponse({'ret': 1, 'msg': '用户已存在'})
