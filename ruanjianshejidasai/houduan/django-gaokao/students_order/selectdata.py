from common.models import MajorType01, MajorType02, College
from django.http import JsonResponse
import json


# 查院校和专业
def select_data(request):
    if request.method == 'POST':
        request_params = json.loads(request.body)
        if request_params.get('action'):
            if request_params['action'] == 'select_college':
                if request_params['college_name']:
                    data = College.objects.filter(name=request_params['college_name'])
                    college_data = []
                    for row in data:
                        college_data.append(
                            {
                                'name': row.name,
                                'college_id': row.id,
                                'address': row.address,
                                'Type_college': ','.join(map(str, row.Type_college))
                            }
                        )
                    return JsonResponse({'ret': 0, 'data': college_data})
                list_order = request_params['college_type']
                data = College.objects.filter(address=request_params['college_address'],
                                              Type_college__contains=list_order)
                college_data = []
                for row in data:
                    college_data.append(
                        {
                            'name': row.name,
                            'college_id': row.id,
                            'address': row.address,
                            'Type_college': ','.join(map(str, row.Type_college))
                        }
                    )
                return JsonResponse({'ret': 0, 'data': college_data})
            elif request_params['action'] == 'select_major':
                if request_params['major_name']:
                    data = MajorType01.objects.filter(major_name=request_params['major_name'])
                    major_data = []
                    for row in data:
                        major_data.append(
                            {
                                'major_code': row.major_code,
                                'major_name': row.major_name,
                                'big_type': row.big_type,
                                'small_type': row.small_type,
                                'major_year': row.major_year,
                                'academic': row.academic,
                                'set': '本科'
                            }
                        )
                    data = MajorType02.objects.filter(major_name=request_params['major_name'])
                    for row in data:
                        major_data.append(
                            {
                                'major_code': row.major_code,
                                'major_name': row.major_name,
                                'big_type': row.big_type,
                                'major_year': row.major_year,
                                'set': '专科'
                            }
                        )
                    return JsonResponse({'ret': 0, 'data': major_data})

                # 门类
                list_order = request_params['major_type']
                if request_params['major_set'] == '本科':
                    data = MajorType01.objects.filter(big_type__in=list_order)
                    major_data = []
                    for row in data:
                        major_data.append(
                            {
                                'major_code': row.major_code,
                                'major_name': row.major_name,
                                'big_type': row.big_type,
                                'small_type': row.small_type,
                                'major_year': row.major_year,
                                'academic': row.academic
                            }
                        )
                    return JsonResponse({'ret': 0, 'data': major_data})
                else:
                    data = MajorType02.objects.filter(big_type__in=list_order)
                    major_data = []
                    for row in data:
                        major_data.append(
                            {
                                'major_code': row.major_code,
                                'major_name': row.major_name,
                                'big_type': row.big_type,
                                'major_year': row.major_year,
                            }
                        )
                    return JsonResponse({'ret': 0, 'data': major_data})
        else:
            return JsonResponse({'ret': 1, 'msg': '缺少信息'})
    else:
        return JsonResponse({'ret': 1, 'msg': '请求错误'})