from django.http import JsonResponse
from common.models import Students, Teachers
import json


def getdata(request):
    '''if request.seession.get('mng'):
        if request.seession['mng'] != 'qwe43rrt':
            return JsonResponse({'ret': 1, 'msg': '权限不足'})
    else:
        return JsonResponse({'ret': 1, 'msg': '权限不足'})'''
    request_params = json.loads(request.body)
    if request_params['action'] == 'get_user':
        stu = Students.objects.all()
        data_list = stu.values_list('account', 'mail')
        data_list = list(data_list)
        stu_list = []
        for account, mail in data_list:
            stu_list.append(
                {
                    'account': account,
                    'mail': mail
                }
            )
        return JsonResponse({'ret': 0, 'data': stu_list})
    else:
        tch = Teachers.objects.all()
        data_list = tch.values_list('account', 'name', 'sex', 'mail', 'phonenumber', 'age', 'major_type', 'advice_num')
        data_list = list(data_list)
        tch_list = []
        for account, name, sex, mail, phonenumber, age, major_type, advice_num in data_list:
            tch_list.append(
                {
                    'account': account,
                    'name': name,
                    'sex': sex,
                    'mail': mail,
                    'phonenumber': phonenumber,
                    'age': age,
                    'major': major_type,
                    'advice_num': advice_num
                }
            )
        return JsonResponse({'ret': 0, 'data': tch_list})
