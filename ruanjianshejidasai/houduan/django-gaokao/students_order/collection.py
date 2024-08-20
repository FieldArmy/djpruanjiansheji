from django.shortcuts import render

# Create your views here.
from django.db.models import F
from django.http import JsonResponse
# 分页库
from django.core.paginator import Paginator
from common.models import Students, College, MajorType01, MajorType02, CollectCollege, CollectMajor01, CollectMajor02
import json


# 对收藏列表的一系列操作
# 收藏院校，专业
def collect_data(request):
    request_params = json.loads(request.body)
    if request_params['action'] == 'collect_college':
        try:
            account = Students.objects.get(account=request_params['account'])
        except:
            return JsonResponse({'ret': 1, 'msg': '用户不存在'})
        try:
            college = College.objects.get(id=request_params['college_id'])
            CollectCollege.objects.create(account=account, college=college)
            return JsonResponse({'ret': 0})
        except:
            return JsonResponse({'ret': 1, 'msg': '收藏失败'})
    elif request_params['action'] == 'collect_major':
        if request_params['major_set'] == '本科':
            try:
                account = Students.objects.get(account=request_params['account'])
            except:
                return JsonResponse({'ret': 1, 'msg': '用户不存在'})
            try:
                major = MajorType01.objects.get(major_code=request_params['major_id'])
                CollectMajor01.objects.create(account=account, major=major)
                return JsonResponse({'ret': 0})
            except:
                return JsonResponse({'ret': 1, 'msg': '收藏失败'})

        elif request_params['major_set'] == '专科':
            try:
                account = Students.objects.get(account=request_params['account'])
            except:
                return JsonResponse({'ret': 1, 'msg': '用户不存在'})
            try:
                major = MajorType02.objects.get(major_code=request_params['major_id'])
                CollectMajor02.objects.create(account=account, major=major)
                return JsonResponse({'ret': 0})
            except:
                return JsonResponse({'ret': 1, 'msg': '收藏失败'})


# 列出院校/专业
def list_collection(request):
    request_params = request.GET
    # 获取收藏
    if request_params['action'] == 'list_college':
        try:
            account = Students.objects.get(account=request_params['account'])
        except:
            return JsonResponse({'ret': 1, 'msg': '用户不存在'})
        data = CollectCollege.objects.filter(account=account)
        if data.exists():
            total = len(data)
            # 生成分页对象
            paginator = Paginator(data, request_params['pagesize'])
            # 获取第几页的信息
            page = paginator.get_page(request_params['pagenum'])
            # 规范返回数据
            retlist = []
            for i in page:
                x = ','.join(map(str, list(i.college.Type_college)))
                retlist.append({"name": i.college.name, "college_id": i.college.id,
                                "address": i.college.address,
                                "Type_college": x})

            return JsonResponse({'ret': 0, 'data': retlist, 'total': total})

        else:
            return JsonResponse({'ret': 1, 'msg': '无记录'})
    else:
        if request_params['major_set'] == '本科':
            try:
                account = Students.objects.get(account=request_params['account'])
            except:
                return JsonResponse({'ret': 1, 'msg': '用户不存在'})
            data = CollectMajor01.objects.filter(account=account)
            if data.exists():
                total = len(data)
                # 生成分页对象
                paginator = Paginator(data, request_params['pagesize'])
                # 获取第几页的信息
                page = paginator.get_page(request_params['pagenum'])
                # 规范返回数据
                retlist = []
                for i in page:
                    retlist.append({"major_code": i.major.major_code, "major_name": i.major.major_name,
                                    "big_type": i.major.big_type,
                                    "small_type": i.major.small_type,
                                    "major_year": i.major.major_year,
                                    "academic": i.major.academic})

                return JsonResponse({'ret': 0, 'data': retlist, 'total': total})

            else:
                return JsonResponse({'ret': 1, 'msg': '无记录'})
        else:
            if request_params['major_set'] == '专科':
                try:
                    account = Students.objects.get(account=request_params['account'])
                except:
                    return JsonResponse({'ret': 1, 'msg': '用户不存在'})
                data = CollectMajor02.objects.filter(account=account)
                if data.exists():
                    total = len(data)
                    # 生成分页对象
                    paginator = Paginator(data, request_params['pagesize'])
                    # 获取第几页的信息
                    page = paginator.get_page(request_params['pagenum'])
                    # 规范返回数据
                    retlist = []
                    for i in page:
                        retlist.append({"major_code": i.major.major_code, "major_name": i.major.major_name,
                                        "big_type": i.major.big_type,
                                        "major_year": i.major.major_year})

                    return JsonResponse({'ret': 0, 'data': retlist, 'total': total})

                else:
                    return JsonResponse({'ret': 1, 'msg': '无记录'})


def del_collection(request):
    request_params = json.loads(request.body)
    if request_params['action'] == 'del_college':
        try:
            CollectCollege.objects.get(college__id=request_params['college_id'], account=request_params['account']).delete()
            return JsonResponse({'ret': 0})
        except:
            return JsonResponse({'ret': 1, 'msg': '删除失败'})
    elif request_params['action'] == 'del_major':
        if request_params['major_set'] == '本科':
            try:
                CollectMajor01.objects.get(major__major_code=request_params['major_id'], account=request_params['account']).delete()
                return JsonResponse({'ret': 0})
            except:
                return JsonResponse({'ret': 1, 'msg': '删除失败'})
        else:
            try:
                CollectMajor02.objects.get(major__major_code=request_params['major_id'], account=request_params['account']).delete()
                return JsonResponse({'ret': 0})
            except:
                return JsonResponse({'ret': 1, 'msg': '删除失败'})
