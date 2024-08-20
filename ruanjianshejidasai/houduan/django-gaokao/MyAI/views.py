# Create your views here.
# views.py
from django.shortcuts import render
from django.http import JsonResponse
import requests
import json


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xiITB8bUZC6vUMSKRSJdIoHe&client_secret=HEF2U8YTXCcG8WeFsYvIjORoSMRzbBVC"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def chatbot_talk(request):
    if request.method == 'POST':
        request_params = json.loads(request.body)
        user_input = request_params['question']
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()

        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        result = json.loads(response.text)
        return JsonResponse({'ret': 0, 'result': result})

