from django.http import JsonResponse
from common.models import Issues, Students
import json


def issue(request):
    request_params = json.loads(request.body)
    try:
        students = Students.objects.get(account=request_params['account'])
    except:
        return JsonResponse({'ret': 1, 'msg': '用户不存在'})
    Issues.objects.create(students=students, issue=request_params['issue'])
    return JsonResponse({'ret': 0})