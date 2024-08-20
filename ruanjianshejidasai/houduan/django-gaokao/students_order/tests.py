import requests
import pprint
import json

li = {
    "action": "rec_list_order",
    "first": "院校优先",
    "like": {
        "sort_by": "综合排序",
        "address": json.dumps('山东'),
        "type": [985],
        "major": [],
        "set": "本科"
    },
    "account": "wcr200215"
}

response = requests.post('http://192.168.43.224:8080/api/students/recommend', json=li)

pprint.pprint(response.json())
