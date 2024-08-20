# Create your views here.
from django.db.models import F, Q, Case, When, IntegerField, ExpressionWrapper
from django.http import JsonResponse

from common.models import Students, Admissions, College
import json


def admissions(request):
    request_params = json.loads(request.body)
    if request_params['action'] == 'rec_list_order':
        # 筛选院校类型
        school_list = request_params['like'].get('type')
        # school_list = json.dumps(school_list, ensure_ascii=False)
        # 筛选
        # 获取用户信息
        try:
            my_account = Students.objects.get(account=request_params['account'])
        except:
            return JsonResponse({'ret': 1, 'msg': '用户不存在'})
        # 判断该账户用户信息是否填写完整
        if not my_account.check_data:
            return JsonResponse({
                'ret': 1,
                'msg': '用户信息填写不完整'})
        # 获取用户选课信息
        class_flag = {
            '物理': 1,
            '化学': 2,
            '生物': 3,
            '地理': 4,
            '历史': 5,
            '政治': 6
        }
        sel_class = list(json.loads(my_account.sel_class))
        # 用来存储选课中没有选的课所对应的序号，因为没有选的课的值必须为False
        sel_list = [1, 2, 3, 4, 5, 6]
        # 非’/‘，筛选条件则是用户未选的科目不可以为True
        for sel in sel_class:
            sel_list.remove(class_flag[sel])
        # 每个序号所对应的属性名
        class_map = Admissions.class_map
        query1 = Q()
        for class1_value in sel_list:
            class1_name = class_map.get(class1_value)
            if class1_name:
                # 这里解包的目的是让键的值可变
                query1 &= Q(**{class1_name: False})

        # ’/‘，筛选条件为用户选的科目不可以全部为False
        sel_list = []
        for sel in sel_class:
            sel_list.append(class_flag[sel])
        query2 = Q()
        for class2_value in sel_list:
            class2_name = class_map.get(class2_value)
            if class2_name:
                # 这里解包的目的是让键的值可变
                query2 &= Q(**{class2_name: False})

        # 生成推荐表
        if request_params['first'] == '院校优先':
            flag1_query = Q()
        # 如果是专业优先
        else:
            flag1_query = Q(major_name__in=request_params['like']['major'])
        if json.loads(request_params['like'].get('address')) == '所有地区':
            flag2_query = Q()
        else:
            flag2_query = Q(college__address=json.loads(request_params['like']['address']))

        # 筛选出三年内的最高和最低位次
        max_ranking = Case(
            # 无论数据存在几年，此方法一直可以找出最大的位次，因为无数据的位置为0
            # 只存在一年数据
            When(
                Q(One_year_ranking=0) & Q(Two_year_ranking=0) & Q(Three_year_ranking__gt=0),
                then=(F('Three_year_ranking') + F('Three_year_ranking') / 10)
            ),
            When(
                Q(One_year_ranking=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking=0),
                then=(F('Two_year_ranking') + F('Two_year_ranking') / 10)
            ),
            When(
                Q(One_year_ranking__gt=0) & Q(Two_year_ranking=0) & Q(Three_year_ranking=0),
                then=(F('One_year_ranking') + F('One_year_ranking') / 10)
            ),
            When(
                Q(One_year_ranking__gte=F('Two_year_ranking')) & Q(Two_year_ranking__gte=F('Three_year_ranking')),
                then=F('One_year_ranking')),
            When(
                Q(One_year_ranking__gte=F('Three_year_ranking')) & Q(
                    Three_year_ranking__gte=F('Two_year_ranking')),
                then=F('One_year_ranking')),
            When(
                Q(Two_year_ranking__gte=F('Three_year_ranking')) & Q(
                    Three_year_ranking__gte=F('One_year_ranking')),
                then=F('Two_year_ranking')),
            When(
                Q(Two_year_ranking__gte=F('One_year_ranking')) & Q(One_year_ranking__gte=F('Three_year_ranking')),
                then=F('Two_year_ranking')),
            default=F('Three_year_ranking'),
            output_field=IntegerField()
        )
        min_ranking = Case(
            # 三年数据全部存在
            When(
                Q(One_year_ranking__gt=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking__gt=0) &
                Q(One_year_ranking__lte=F('Two_year_ranking')) & Q(Two_year_ranking__lte=F('Three_year_ranking')),
                then=F('One_year_ranking')),
            When(
                Q(One_year_ranking__gt=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking__gt=0) &
                Q(One_year_ranking__lte=F('Three_year_ranking')) & Q(
                    Three_year_ranking__lte=F('Two_year_ranking')),
                then=F('One_year_ranking')),
            When(
                Q(One_year_ranking__gt=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking__gt=0) &
                Q(Two_year_ranking__lte=F('Three_year_ranking')) & Q(
                    Three_year_ranking__lte=F('One_year_ranking')),
                then=F('Two_year_ranking')),
            When(
                Q(One_year_ranking__gt=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking__gt=0) &
                Q(Two_year_ranking__lte=F('One_year_ranking')) & Q(One_year_ranking__lte=F('Three_year_ranking')),
                then=F('Two_year_ranking')),
            # 只有两年的数据
            When(
                Q(One_year_ranking=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking__gt=0)
                & Q(Two_year_ranking__gte=F('Three_year_ranking')),
                then=F('Three_year_ranking')
            ),
            When(
                Q(Two_year_ranking=0) & Q(One_year_ranking__gt=0) & Q(Three_year_ranking__gt=0)
                & Q(One_year_ranking__gte=F('Three_year_ranking')),
                then=F('Three_year_ranking')
            ),
            When(
                Q(Three_year_ranking=0) & Q(Two_year_ranking__gt=0) & Q(One_year_ranking__gt=0)
                & Q(Two_year_ranking__gte=F('One_year_ranking')),
                then=F('One_year_ranking')
            ),
            When(
                Q(One_year_ranking=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking__gt=0)
                & Q(Two_year_ranking__lte=F('Three_year_ranking')),
                then=F('Two_year_ranking')
            ),
            When(
                Q(Two_year_ranking=0) & Q(One_year_ranking__gt=0) & Q(Three_year_ranking__gt=0)
                & Q(One_year_ranking__lte=F('Three_year_ranking')),
                then=F('One_year_ranking')
            ),
            When(
                Q(Three_year_ranking=0) & Q(Two_year_ranking__gt=0) & Q(One_year_ranking__gt=0)
                & Q(Two_year_ranking__lte=F('One_year_ranking')),
                then=F('Two_year_ranking')
            ),
            # 只存在一年数据
            When(
                Q(One_year_ranking=0) & Q(Two_year_ranking=0) & Q(Three_year_ranking__gt=0),
                then=(F('Three_year_ranking') - F('Three_year_ranking') / 10)
            ),
            When(
                Q(One_year_ranking=0) & Q(Two_year_ranking__gt=0) & Q(Three_year_ranking=0),
                then=(F('Two_year_ranking') - F('Two_year_ranking') / 10)
            ),
            When(
                Q(One_year_ranking__gt=0) & Q(Two_year_ranking=0) & Q(Three_year_ranking=0),
                then=(F('One_year_ranking') - F('One_year_ranking') / 10)
            ),
            default=F('Three_year_ranking'),
            output_field=IntegerField()
        )
        # 计算最大推荐位次
        expression = ExpressionWrapper(F('max_ranking') + (F('max_ranking') - F('min_ranking')),
                                       output_field=IntegerField())
        # 根据上述内容对数据库筛选
        recommand = Admissions.objects.annotate(
            # 录取率为20%的所在位次
            max_ranking=max_ranking, min_ranking=min_ranking,
            lastRanking=expression
        ).filter(
            ((query1 & Q(flag_class=False)) | (~query2 & Q(flag_class=True)))
            & Q(major_set=request_params['like']['set'])
            & Q(college__Type_college__contains=school_list)
            & Q(lastRanking__gte=my_account.ranking)
            & flag1_query & flag2_query
        )

        # 根据筛选出的各条志愿，找到其对应的学校,外键反向过滤,可能有问题
        school_data = College.objects.filter(admissions__in=recommand).distinct()
        # 最终的响应消息体
        college_major = []
        # 用于在创建好的框架上插值不用重复遍历
        flag = {}
        num = 0
        # 先将响应消息体的基本格式创建出来
        for x in school_data:
            college_major.append({
                "college_name": x.name,
                "college_id": x.id,
                "address": x.address,
                "type": '',
                "plan": 0,
                "low_grades": 800,
                "low_ranking": 0,
                "college_percent": 0,
                "majors": []
            })
            # 表示该院校位于列表的第几个位置
            flag[x.id] = num
            # 添加院校类型
            college_major[num]['type'] = ','.join(map(str, x.Type_college))
            num += 1

        # 匹配专业表
        for y in recommand:
            y_id = y.college.id
            ym_id = y.major_id
            y_grades = y.One_year_greads
            y_ranking = y.One_year_ranking
            # 被该专业录取的概率
            y_percent = (0.2 + (y.lastRanking - my_account.ranking) // (
                    (3 * (y.max_ranking - y.min_ranking)) / 80) * 0.01) * 100 // 1
            if y_percent > 99:
                y_percent = 99

            if college_major[flag.get(y_id)].get('low_grades') > y_grades and (y_grades != 0):
                college_major[flag.get(y_id)]['low_grades'] = y_grades
            if college_major[flag.get(y_id)].get('low_ranking') < y_ranking:
                college_major[flag.get(y_id)]['low_ranking'] = y_ranking
            if college_major[flag.get(y_id)].get('college_percent') < y_percent:
                college_major[flag.get(y_id)]['college_percent'] = y_percent
            college_major[flag.get(y_id)]['plan'] += y.major_num
            # 获取这个专业的相关信息
            major_data = {
                'major_name': y.major_name,
                'major_id': ym_id,
                'major_year': y.major_year,
                'major_pay': y.major_pay,
                'major_plan': y.major_num,
                'major_object': [],
                'major_grades': y_grades,
                'major_ranking': y_ranking,
                'major_percent': y_percent,
                'major_set': y.major_set
            }
            # 添加必选科目
            type_list = []
            if y.wuli_class:
                type_list.append('物理')
            if y.huaxue_class:
                type_list.append('化学')
            if y.shengwu_class:
                type_list.append('生物')
            if y.dili_class:
                type_list.append('地理')
            if y.lishi_class:
                type_list.append('历史')
            if y.zhengzhi_class:
                type_list.append('政治')
            # 如果对各个科目都没有限制
            if not type_list:
                type_list.append('不限科目')
            if y.flag_class:
                major_data['major_object'] = ','.join(type_list)
            else:
                major_data['major_object'] = '/'.join(type_list)
            college_major[flag.get(y_id)]['majors'].append(major_data)
        # 找到所有没有数据的院校专业
        zero_major = Admissions.objects.filter(
            Q(college__in=school_data) & Q(One_year_ranking=0) & Q(Two_year_ranking=0) &
            Q(Three_year_ranking=0) &
            ((query1 & Q(flag_class=False)) | ~query2)
            & flag1_query & flag2_query)
        for z in zero_major:
            # 获取这个专业的相关信息
            major_data = {
                'major_name': z.major_name,
                'major_id': z.major_id,
                'major_year': z.major_year,
                'major_pay': z.major_pay,
                'major_plan': z.major_num,
                'major_object': [],
                'major_grades': college_major[flag.get(z.college.id)]['low_grades'],
                'major_ranking': college_major[flag.get(z.college.id)]['low_ranking'],
                'major_percent': college_major[flag.get(z.college.id)]['college_percent'],
                'major_set': z.major_set
            }
            # 添加必选科目
            type_list = []
            if z.wuli_class:
                type_list.append('物理')
            if z.huaxue_class:
                type_list.append('化学')
            if z.shengwu_class:
                type_list.append('生物')
            if z.dili_class:
                type_list.append('地理')
            if z.lishi_class:
                type_list.append('历史')
            if z.zhengzhi_class:
                type_list.append('政治')
            # 如果对各个科目都没有限制
            if not type_list:
                type_list.append('不限科目')
            if z.flag_class:
                major_data['major_object'] = ','.join(type_list)
            else:
                major_data['major_object'] = '/'.join(type_list)
            college_major[flag.get(z.college.id)]['majors'].append(major_data)
        return JsonResponse({'ret': 0, 'college_major': college_major})

    else:
        return JsonResponse({'ret': 1, 'msg': '不存在该请求'})
