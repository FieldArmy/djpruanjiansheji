from django.utils.deprecation import MiddlewareMixin
import json
from django.http import JsonResponse
from django.core.cache import cache


class CheckSignin(MiddlewareMixin):
    def process_request(self, request):
        if request.method == 'GET':
            request_params = request.GET
        else:
            request_params = json.loads(request.body)
        if 'action' in request_params:
            if 'account' not in request.session:
                return JsonResponse({
                    'ret': 302,
                    'msg': '未登录'},
                    #status=302
                )
            else:
                if request.session.get('mng'):
                    request.session['mng'] = 'qwe43rrt'
                if request.session.get('tch'):
                    request.seession['tch'] = 'ww33ert'
                check_id = cache.get(request.session['account'])
                if check_id:
                    if check_id != request.session.session_key:
                        request.session.flush()
                        return JsonResponse({
                            'ret': 302,
                            'msg': '您的账户已经在另一台设备上登录'}
                            #status=302
                        )
                else:
                    return JsonResponse({
                        'ret': 302,
                        'msg': '用户不存在'}
                        #status=302
                    )
        else:
            pass

