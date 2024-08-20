from django.http import JsonResponse
from common.models import Manager
from django.db.models import Q
from django.core.cache import cache
import json


# 登录
def sign_in(request):
    request_params = json.loads(request.body)
    try:
        mng = Manager.objects.get(Q(account=request_params['account']))
    except:
        return JsonResponse({'ret': 1, 'msg': '用户名不存在'})
    # 密码鉴别
    if request_params['password'] == mng.password:
        session = request.session
        # 保存用户登录账号
        session['account'] = mng.account
        session['mng'] = 'manager'
        # 保存当前账号登录所使用的session_id
        cache.set(mng.account, session.session_key)
        return JsonResponse({'ret': 0})
    else:
        # 密码验证失败
        return JsonResponse({'ret': 1, 'msg': '密码错误'})
