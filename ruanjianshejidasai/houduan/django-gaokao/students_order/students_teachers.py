from django.http import JsonResponse
from common.models import Teachers, Students, Advice
import json


# 用户获取咨询师信息
def get_teacher(request):
    request_params = json.loads(request.body)
    if request_params['action'] == 'get_teacher':
        tch = Teachers.objects.all()
        data_list = tch.values_list('account', 'name', 'sex', 'mail', 'phonenumber', 'age', 'text', 'advice_num',
                                    'major_type')
        data_list = list(data_list)
        tch_list = []
        for account, name, sex, mail, phonenumber, age, text, advice_num, major in data_list:
            tch_list.append(
                {
                    'account': account,
                    'name': name,
                    'sex': sex,
                    'mail': mail,
                    'phonenumber': phonenumber,
                    'age': age,
                    'text': text,
                    'advice_num': advice_num,
                    'major': major
                }
            )
        return JsonResponse({'ret': 0, 'data': tch_list})
    else:
        return JsonResponse({'ret': 1, 'msg': '请求不存在'})


# 用户提交咨询信息
def give_question(request):
    request_params = json.loads(request.body)
    if request_params['action'] == 'give_question':
        try:
            teacher = Teachers.objects.get(account=request_params['tch_code'])
            student = Students.objects.get(account=request_params['account'])
        except:
            return JsonResponse({'ret': 1, 'msg': '该咨询师或用户不存在'})
        Advice.objects.create(students=student, teachers=teacher, question=request_params['question'])
        teacher.advice_num += 1
        teacher.save()
        return JsonResponse({'ret': 0})
    else:
        return JsonResponse({'ret': 1, 'msg': '请求不存在'})


# 用户获取咨询回复
def get_question(request):
    request_params = json.loads(request.body)
    if request_params['action'] == 'get_question':
        try:
            student = Students.objects.get(account=request_params['account'])
        except:
            return JsonResponse({'ret': 1, 'msg': '用户不存在'})
        advice = Advice.objects.filter(students=student)
        question = []
        for data in advice:
            question.append({
                "code": data.id,
                "question": data.question,
                "time": data.time,
                "name": data.teachers.name,
                "advice": data.advice
            })
        return JsonResponse({'ret': 0, 'question': question})
    else:
        return JsonResponse({'ret': 1, 'msg': '请求不存在'})
