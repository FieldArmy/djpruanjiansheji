from django.test import TestCase, Client
from common.models import Students
from django.contrib.auth.hashers import make_password
import json

class SignInTest(TestCase):
    def setUp(self):
        self.client = Client()
        password = make_password('12345678')
        Students.objects.create(account='12345678', password=password, mail='1668572316@qq.com')

    def test_sign_in_success(self):
        # 构造登录请求的数据
        login_data = {
            "account": '12345678',
            "password": "12345678"
        }
        # 使用Client发送POST请求
        response = self.client.post('/api/students/signin', json.dumps(login_data), content_type='application/json')
        # 断言响应状态码为200
        self.assertEqual(response.status_code, 200)
        # 断言返回的JSON数据中ret为0，表示登录成功
        self.assertEqual(response.json()['ret'], 0)

    def test_sign_in_failure(self):
        # 构造登录请求的数据，使用错误的密码
        login_data = {
            'account': 'testuser',
            'password': 'wrongpassword'
        }
        # 使用Client发送POST请求
        response = self.client.post('/api/students/signin', json.dumps(login_data), content_type='application/json')
        # 断言响应状态码为200
        self.assertEqual(response.status_code, 200)
        # 断言返回的JSON数据中ret为1，表示登录失败
        self.assertEqual(response.json()['ret'], 1)
