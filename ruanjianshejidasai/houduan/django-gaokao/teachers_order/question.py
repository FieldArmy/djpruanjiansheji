from django.http import JsonResponse
from common.models import Teachers, Advice
import json


# 咨询师获取和回复咨询信息
def question(request):
    '''if request.seession.get('tch'):
        if request.seession['tch'] != 'ww33ert':
            return JsonResponse({'ret': 1, 'msg': '权限不足'})
    else:
        return JsonResponse({'ret': 1, 'msg': '权限不足'})'''
    request_params = json.loads(request.body)
    if request_params['action'] == 'get_question':
        advice = Advice.objects.filter(teachers__account=request_params['account'])
        question01 = []
        question02 = []
        for data in advice:
            if data.advice == '暂未收到回复':
                question02.append({
                    "code": data.id,
                    "account": data.students.account,
                    "question": data.question,
                    "time": data.time,
                    "advice": data.advice
                })
            else:
                question01.append({
                    "code": data.id,
                    "account": data.students.account,
                    "question": data.question,
                    "time": data.time,
                    "advice": data.advice
                })
        return JsonResponse({'ret': 0, 'question01': question01, 'question02': question02})
    elif request_params['action'] == 'set_question':
        try:
            advice = Advice.objects.get(id=request_params['code'])
        except:
            return JsonResponse({'ret': 1, 'msg': '该问题不存在'})
        advice.advice = request_params['advice']
        advice.save()
        return JsonResponse({'ret': 0})
