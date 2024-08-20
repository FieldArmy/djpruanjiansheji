from django.http import JsonResponse
from common.models import College, Admissions


def getdata(request):
    request_params = request.GET
    if request_params['action'] == 'list_college':
        college = College.objects.all()
        name_list = college.values_list('name', flat=True)
        name_list = list(name_list)
        #--------------------------------------------------------这里有修改
        name = []
        for i in name_list:
            name.append({
                'value': i
            })
        return JsonResponse({'ret': 0, 'college_name': name})
    else:
        admissions = Admissions.objects.all()
        values = admissions.values('major_name').distinct()
        name_list = values.values_list('major_name', flat=True)
        name_list = list(name_list)
        # --------------------------------------------------------这里有修改
        name = []
        for i in name_list:
            name.append({
                'value': i
            })
        return JsonResponse({'ret': 0, 'major_name': name})
