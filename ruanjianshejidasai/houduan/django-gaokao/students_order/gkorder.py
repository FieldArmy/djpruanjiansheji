from django.shortcuts import render

# Create your views here.
from django.db.models import F
from django.http import JsonResponse
# 分页库
from django.core.paginator import Paginator
from common.models import Students, Gkorder
import json


def list_order(request):
    request_params = request.GET
    # 获取志愿
    data = Gkorder.objects.filter(account=request_params['account'], major_set=request_params['major_set']).order_by(
        'Gk_id')
    if data.exists():
        total = len(data)
        # 生成分页对象
        paginator = Paginator(data, request_params['pagesize'])
        # 获取第几页的信息
        page = paginator.get_page(request_params['pagenum'])
        # 规范返回数据
        retlist = []
        for i in page:
            retlist.append({"order_id": i.Gk_id, "college_name": i.college_name, "college_id": i.college_id,
                            "major_name": i.major_name, "major_id": i.major_id})

        return JsonResponse({'ret': 0, 'retlist': retlist, 'total': total})

    else:
        return JsonResponse({'ret': 1, 'msg': '无记录'})


def add_order(request):
    request_params = json.loads(request.body)
    data = Gkorder.objects.filter(account=request_params['account'], major_set=request_params['major_set'])
    # 判断是否为第一个志愿
    if data.exists():
        length = len(data)
    else:
        length = 0
    if length + 1 > 96:
        return JsonResponse({'ret': 1, 'msg': '志愿超过上限'})
    try:
        new_data = Gkorder(Gk_id=length + 1, account=Students.objects.get(account=request_params['account']),
                           college_id=request_params['data']['college_id'],
                           major_id=request_params['data']['major_id'],
                           college_name=request_params['data']['college_name'],
                           major_name=request_params['data']['major_name'],
                           major_set=request_params['major_set'])
        new_data.save()
        return JsonResponse({'ret': 0})
    except:
        return JsonResponse({'ret': 1, 'msg': '该条志愿已经填写过'})


def del_order(request):
    request_params = json.loads(request.body)
    if request_params['action'] == 'del_order_all':
        try:
            # 从表中找到相应的记录
            data = Gkorder.objects.filter(account=request_params['account'], major_set=request_params['major_set'])
            data.delete()
            return JsonResponse({'ret': 0})
        except:
            return JsonResponse({'ret': 1, 'msg': '无法删除'})
    try:
        # 从表中找到相应的记录
        data = Gkorder.objects.get(account=request_params['account'], major_set=request_params['major_set'],
                                   Gk_id=request_params['order_id'])
    except:
        return JsonResponse({'ret': 1, 'msg': '无法删除'})
    data.delete()
    # 删除之后，其排在它后面的值向前补一位
    s = Gkorder.objects.filter(account=request_params['account'], Gk_id__gt=request_params['order_id']). \
        update(Gk_id=F('Gk_id') - 1)  # __gt表示大于
    return JsonResponse({'ret': 0})


# 路径分配
def gkorder_dispather(request):
    if request.method == 'GET':
        request_params = request.GET
    elif request.method in ['POST', 'DELETE']:
        request_params = json.loads(request.body)
    else:
        return JsonResponse({'ret': 2, 'msg': '不支持该类型http请求'})

    # 分配给不同函数进行处理
    # 获取行动和账户
    action = request_params['action']
    account = request_params['account']
    # 判断用户是否存在
    try:
        ins = Students.objects.get(account=account)
    except:
        return JsonResponse({'ret': 3, 'msg': '用户不存在'})
    # 判断该账户用户信息是否填写完整
    if not ins.check_data:
        return JsonResponse({
            'ret': 302,
            'msg': '用户信息填写不完整'},
            status=302)
    if action == 'list_order':
        return list_order(request)
    elif action == 'add_order':
        return add_order(request)
    else:
        return del_order(request)
