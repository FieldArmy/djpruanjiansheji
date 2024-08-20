from django.http import JsonResponse
from common.models import Issues
import json


def get_issue(request):
    '''if request.seession.get('mng'):
            if request.seession['mng'] != 'qwe43rrt':
                return JsonResponse({'ret': 1, 'msg': '权限不足'})
        else:
            return JsonResponse({'ret': 1, 'msg': '权限不足'})'''
    request_params = json.loads(request.body)
    if request_params['action'] != 'get_issue':
        return JsonResponse({'ret': 1, 'msg': '请求错误'})
    issue = Issues.objects.all()
    data_list = issue.values_list('issue', 'time', 'students__account')
    data_list = list(data_list)
    issue_list = []
    for issue, time, students_account in data_list:
        issue_list.append({
            'issue': issue,
            'time': time,
            'students_account': students_account
        })
    return JsonResponse({'ret': 0, 'data': issue_list})