from django.http import JsonResponse
from common.models import Students
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
# 创建会话对象
from django.contrib.sessions.backends.cache import SessionStore
# 发送邮件库
from django.core.mail import send_mail

from django.core.cache import cache
# 过滤器
from django.core.exceptions import ValidationError
import random
import string
import json

from django.views.decorators.cache import never_cache


def generate_random_code(length=6):
    # 生成指定长度的随机验证码
    return ''.join(random.choices(string.digits, k=length))


# 发送邮件
def send_verification_code(email):
    # 生成验证码
    code = generate_random_code()

    # 邮件内容
    subject = '验证码'
    message = f'您的验证码是：{code}(一分钟内有效),若非本人操作请忽略此信息'
    from_email = '2229005080@qq.com'  # 发件人邮箱
    recipient_list = [email]
    # 发送邮件
    send_mail(subject, message, from_email, recipient_list)
    return code


# 发送验证码
def give_code(request):
    request_params = json.loads(request.body)
    # 发送验证码
    code = send_verification_code(request_params['mail'])
    # 将获取的验证码放入缓存
    # 创建一个会话对象并将验证码存储在其中
    session = SessionStore()
    session['code'] = code
    session.set_expiry(60)  # 设置会话过期时间为60秒
    session.save()
    return JsonResponse({'ret': 0, 'timeout': 60, 'session_id': session.session_key})


# 注册
def sign_up(request):
    request_params = json.loads(request.body)
    session_id = request_params.get('session_id', None)
    if True:
        # 通过会话ID从缓存中获取验证码
        session = SessionStore(session_key=session_id)
        if True:
           # code = session['code']
            if True:
                # 验证码验证成功，进行注册操作
                Stu = Students.objects.filter(account=request_params['account'])
                # 如果该账户没有被注册过
                if not Stu.exists():
                    try:
                        hash_password = make_password(request_params['password'])
                        Students.objects.create(account=request_params['account'], password=hash_password,
                                                mail=request_params['mail'],
                                                check_data=False)
                        session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                        return JsonResponse({'ret': 0})
                    except:
                        session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                        return JsonResponse({'ret': 1, 'msg': '该邮箱已被注册'})
                else:
                    session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                    return JsonResponse({'ret': 1, 'msg': '该账户已存在'})
            else:
                session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                return JsonResponse({'ret': 1, 'msg': '验证失败'})
        else:
            session.delete()  # 删除这条注册数据，防止与登录的数据冲突
            return JsonResponse({'ret': 1, 'msg': '验证码不存在'})
    else:
        return JsonResponse({'ret': 1, 'msg': '缺少会话ID'})


# 登录
def sign_in(request):
    request_params = json.loads(request.body)
    # 可以选择用户名登录或者邮箱登录
    try:
        stu = Students.objects.get(
            Q(account=request_params['account']) | Q(mail=request_params['account']))  # 必须限制用户名不可以是邮箱格式
    except Students.DoesNotExist as e:
        return JsonResponse({'ret': 1, 'msg': '用户名不存在'})
    # 密码鉴别
    if check_password(request_params['password'], stu.password):
        session = request.session
        # 保存用户登录账号
        session['account'] = stu.account
        # 保存当前账号登录所使用的session_id
        #print(session.session_key)
        cache.set(stu.account, session.session_key, timeout=60*60*24*7)
        return JsonResponse({'ret': 0})
    else:
        # 密码验证失败
        return JsonResponse({'ret': 1, 'msg': '密码错误'})


# 登出
def sign_out(request):
    request.session.flush()
    # 可以在此处执行其他注销后的逻辑，如重定向到登录页面或其他页面
    return JsonResponse({'ret': 0, 'msg': '注销成功'})


# 找回密码
def find_password(request):
    request_params = json.loads(request.body)
    session_id = request_params.get('session_id', None)
    if True:
        # 通过会话ID从缓存中获取验证码
        session = SessionStore(session_key=session_id)
        if True:
            #code = session['code']
            if True:
                # 验证码验证成功，进行注册操作
                stu = Students.objects.filter(account=request_params['account']).first()
                # 如果存在此账号
                if stu:
                    try:
                        # 设置新的密码
                        hash_password = make_password(request_params['password'])
                        stu.password = hash_password
                        stu.save()
                        session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                        return JsonResponse({'ret': 0})
                    except:
                        session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                        return JsonResponse({'ret': 1, 'msg': '密码修改失败'})
                else:
                    session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                    return JsonResponse({'ret': 1, 'msg': '该账户不存在'})
            else:
                session.delete()  # 删除这条注册数据，防止与登录的数据冲突
                return JsonResponse({'ret': 1, 'msg': '验证失败'})
        else:
            session.delete()  # 删除这条注册数据，防止与登录的数据冲突
            return JsonResponse({'ret': 1, 'msg': '验证码不存在'})
    else:
        return JsonResponse({'ret': 1, 'msg': '缺少会话ID'})

