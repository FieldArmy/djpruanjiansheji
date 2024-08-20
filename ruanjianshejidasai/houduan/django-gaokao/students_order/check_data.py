# 校验数据是否完整
from django.http import JsonResponse
from common.models import Students


def check_data(request):
    request_params = request.GET
    try:
        student = Students.objects.get(account=request_params['account'])
    except:
        return JsonResponse({'ret': 1, 'msg': '用户不存在'})
    if student.check_data:
        return JsonResponse({'ret': 0})
    else:
        return JsonResponse({'ret': 1, 'msg': '请考生先填写信息'})
