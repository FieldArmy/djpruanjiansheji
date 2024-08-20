from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from common.models import Students, Admissions, College, Gkorder
from .my_data import ONE_grades_one_ranking, address, Shandong
import json
# 汉字转拼音
from xpinyin import Pinyin

from django.core.cache import cache


# 操作Students表


def grades(request):
    if request.method == 'POST':
        request_params = json.loads(request.body)
        msg = request_params
        if msg['stu_grd'] <= 750:
            # 该分数的一分一段表
            rank = ONE_grades_one_ranking.list_order.get(msg['stu_grd'], None)
            if rank:
                # rank为该分数的位次区间
                if rank[0] <= msg['ranking'] < rank[1]:
                    qs = Students.objects.filter(account=msg['account']).first()
                    if qs:
                        # 这里主键不发生变化
                        p = Pinyin()
                        qs.stu_grd = msg['stu_grd']
                        try:
                            qs.address = address.provinces[msg['address']]
                        except:
                            return JsonResponse({'set': 5, 'msg': '该省份不存在'})
                        qs.sid = p.get_pinyin(msg['id'], '')
                        qs.ranking = msg['ranking']
                        qs.sel_class = json.dumps(msg['subject'])
                        qs.check_data = True
                        qs.save()
                        # 给与响应消息

                        return JsonResponse({"ret": 0, "gk_first": Shandong.msg['F1'], "gk_second": Shandong.msg['S2'],
                                             "gk_third": Shandong.msg['T3'],
                                             "gk_percentage": msg['stu_grd'] / Shandong.msg['num'],
                                             "subject": request_params['subject'],
                                             "ranking": request_params['ranking'],
                                             "stu_grd": request_params['stu_grd']})
                    else:
                        return JsonResponse({"ret": 4, "msg": "您还没有登录"})
                else:
                    return JsonResponse({"ret": 3, "msg": f"您所填写的分数与位次不匹配,应该为{rank[0]}到{rank[1]}之间", "re_ranking": rank})
            else:
                return JsonResponse({"ret": 2, "msg": "没有找到对应分数的一分一段表"})
        else:
            return JsonResponse({'ret': 1, 'msg': '您所填写的分数不存在'})
    elif request.method == 'GET':
        request_params = request.GET
        if request_params['action'] == 'get_stu':
            try:
                student = Students.objects.get(account=request_params['account'])
            except:
                return JsonResponse({'ret': 1, 'msg': '用户不存在'})
            return JsonResponse({"ret": 0, "gk_first": Shandong.msg['F1'], "gk_second": Shandong.msg['S2'],
                                 "gk_third": Shandong.msg['T3'],
                                 "gk_percentage": student.ranking / Shandong.msg['num'],
                                 "subject": json.loads(student.sel_class),
                                 "ranking": student.ranking,
                                 "stu_grd": student.stu_grd})

        else:
            return JsonResponse({'ret': 1, 'msg': '请求不存在'})

    else:
        return JsonResponse({'ret': 1, 'msg': '请求不存在'})