API接口文档
本接口用于高考志愿填报系统用户前后端之间的数据交互。
在此接口中，所有的请求、响应的消息体均采用UTF8.
消息体均采用json格式
响应消息体json中，ret字段为0表示操作成功，其他均为操作失败。
如果操作失败，会有msg字段，内容为字符串，表示失败原因。
1. GET：获取资源
2、POST：传输实体主体
3、PUT：传输文件
4、HEAD：获得报文首部
5、DELETE：删除文件


管理员：
#管理员登录
请求消息
POST /api/manager/signin HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“account”: “xxxxxxxxx”,
“password”: “xxxxxxxx”
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0
}
#管理员获取用户信息
请求消息
POST /api/manager/getuser HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “get_user”,
“account”: “xxxxxxxxx”,
“set_mag”: “manager”,
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“data”: [{“account”: “xxxxxx”,
“mail“：”xxxxxx“},{…},{…}] #列表
}
#管理员获取咨询师信息
请求消息
POST /api/manager/getteacher HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “get_teacher”,
“account”: “xxxxxxxxx”,
“set_mag”: “manager”
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“data”: [{
				“account“：”xxxxxx“,
“name”: “xxxxxx”,
“sex”:”男”,
“mail”:”xxxxxxx”,
“phonenumber”:”xxxxxx”，
“age”：38，
“major”:”哲学”,
“advice_num”: “2”#被访问次数
},{…},{…}] #列表形式
}

#管理员添加咨询师信息
请求消息
POST /api/manager/addteacher HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “add_teacher”,
“account”: “xxxxxxxxx”,
“set_mag”: “manager”,
“tch_account“：”xxxxxx“,
“tch_password”: ”xxxxxxx”,
“name”: “xxxxxx”,
“sex”:”男”,
“mail”:”xxxxxxx”,
“phonenumber”:”xxxxxx”，
“age”：38，
“major”:”哲学”,
“major_set“：”本科“
“text“: “xxxxxx” # 个人简介
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{“ret”: 0,}


#管理员删除用户
请求消息
DELETE /api/manager/deluser HTTP/1.1
Content-Type: application/json
请求参数
{
	“action”: “del_user”,
	“account”: “12345678”,
“set_mag”: “manager”，
“account_user”: “xxxxxxxxx”, #要删除的用户账号
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0
}

#管理员删除咨询师
请求消息
DELETE /api/manager/delteacher HTTP/1.1
Content-Type: application/json
请求参数
{
	“action”: “del_teacher”,
	“account”: “12345678”,
“set_mag”: “manager”，
“account_teacher”: “xxxxxxxxx”, #要删除的咨询师账号
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0
}
#查看用户反馈
请求消息
POST /api/manager/getissue HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“account”: “xxxxxxxxx”,
“action”: “get_issue”
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“data”: [
{
“issue”: “xxxxxx”,
“time”:”xxxxxxx”,
“students_account”: “xxxxxxxx”
},{….},{….}
]
}


咨询师：
#咨询师登录
请求消息
POST /api/teachers/signin HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“account”: “xxxxxxxxx”,
“password”: “xxxxxxxx”
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0
}
#咨询师获取咨询信息
请求消息
POST /api/teachers/getquestion HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “get_question”,
“account”: “xxxxxxxxx”,
“set_tch”: “teacher”
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“question01”: [{
				“code“： 23，#问题编码
“account”: “xxxxxx”,#用户账号
“question”:”xxxxxx”,
“time”:”xxxxxxx”,
“advice”:”xxxxxx”},{…},{…}] # 已经解决的问题 ，
“question02”: [{
				“code“： 18，#问题编码
“account”: “xxxxxx”, #用户账号
“question”:”xxxxxx”,
“time”:”xxxxxxx”,
“advice”:”xxxxxx”},{…},{…}] # 未经解决的问题

}

#咨询师回答咨询信息
请求消息
POST /api/teachers/setquestion HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “set_question”,
“account”: “xxxxxxxxx”,
“set_tch”: “teacher”,
“code“： 23，#问题编码
“advice”:”xxxxxx”#回复
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0
}
#咨询师获取个人信息
请求消息
POST /api/teachers/getteachers HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “get_teachers”,
“account”: “xxxxxxxxx”,
“set_tch”: “teacher”
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“data”: {“name”: “xxxxxx”,
“sex”:”男”,
“mail”:”xxxxxxx”,
“phonenumber”:”xxxxxx”，
“age”：38，
“major”:”哲学”}
}

#咨询师修改个人信息
请求消息
POST /api/teachers/setteachers HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “set_teachers”,
“account”: “xxxxxxxxx”,
“set_tch”: “teacher”，
“name”: “xxxxxx”,
“sex”:”男”,
“mail”:”xxxxxxx”,
“phonenumber”:”xxxxxx”，
“age”：38，
“major”:”哲学”
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
}


用户提交反馈问题：
请求消息
POST /api/students/giveissue HTTP/1.1
Content-Type: application/json

请求参数
{
“action”：“give_issue”,
“account”: “xxxxxxxx”,
“issue”: “xxxxxxxx”
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
}

用户获取咨询师信息：
请求消息
POST /api/students/getteacher HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “get_teacher”,
“account”: “xxxxxxxxx”
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“data”: [{
				“account“：”xxxxxx“, #咨询师的账号
“name”: “xxxxxx”,
“sex”:”男”,
“mail”:”xxxxxxx”,
“phonenumber”:”xxxxxx”，
“age”：38，
“major”:”哲学”,
“text”: “xxxxxxxx” # 个人简介
},{…},{…}] #列表形式
}
用户提交咨询信息：
请求消息
POST /api/students/givequestion HTTP/1.1
Content-Type: application/json

请求参数
{
“action”：“give_question”,
“account”: “xxxxxxxx”,
“question”: “xxxxxxxx”，
“tch_code”：“xxxxxx”，# 所选择的咨询师的账号
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
}
用户获取咨询回复：
请求消息
POST /api/students/getquestion HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“action”: “get_question”,
“account”: “xxxxxxxxx”
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“data”: [{
				“code”：78，#问题编码
“name”: “xxxxxx”,
“question“：”xxxxxxx“，
“time”：“xxxxx”，#反馈时间
“advice”:”xxxxxx” #回复内容
},{…},{…}] #列表形式
}

获取院校照片：
请求消息
GET /api/students/jepg/<str:filename> HTTP/1.1
Content-Type: image/jpeg
请求参数
响应消息
HTTP/1.1 200 OK
Content-Type: image/jpeg

查院校/专业：
POST api/students/selectdata HTTP/1.1
Content-Type: application/json
{
“action”：“select_college”，# select_major
“college_address”: “山东”, 
“college_name”：“山东大学”，#具体搜索，如果不进行具体搜索，为空即可
“college_type”: [], #包含院校所有的类型，列表形式
“major_set”: “本科”,
“major_type”: []， # 专业门类,列表形式
“major_name”：“信息管理与信息系统”，#具体搜索
“account”: “xxxxxxx”
}
action如果选择了学校，专业部分为空，选择了专业，院校部分为空

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
    "ret": 0,
    "data": [
        {
            "name": "山东大学",
            "college_id": "A422",
            "address": "山东",
            "Type_college": [
                "普通本科",
                985,
                211,
                "双一流",
                "公办",
                "综合类"
            ]
        },{…},{…}]
}或(专科)
{
    "ret": 0,
    "data": [
        {
            "major_code": "410101",
            "major_name": "种子生产与经营",
            "big_type": "农林牧渔大类", #大类
            "major_year": "三年"，
	  	“set“：专科 #具体查询时反馈
        },{…},{…}]
}或(本科)
{
    "ret": 0,
    "data": [
        {
            "major_code": "120101",
            "major_name": "管理科学",
            "big_type": "管理学", #大类
            "small_type": "管理科学与工程类", #小类
            "major_year": "五年，四年",
            "academic": "理学，管理学"，
	“set“：本科 #具体查询时反馈
        },{…},{…}]
}

收藏院校/专业：
POST api/students/collectdata HTTP/1.1
Content-Type: application/json
{
“action”：“collect_college”，# collect_major
“college_id”: “A444”, 
“major_set”: “本科”,
“major_id”: “40441”， 
“account”: “xxxxxxx”
}
action如果选择了学校，专业部分为空，选择了专业，院校部分为空

响应消息
HTTP/1.1 200 OK
Content-Type: application/json
响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0
}

获取收藏的院校/专业
请求消息
GET /api/students/listcollection HTTP/1.1

请求参数
action为必填项，值为list_college或list_major
account为必填项，值为该账户
pagesize 必填，分页的每页获取多少条记录
pagenum 必填，获取第几页的信息
major_set : 设为本科或专科

响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
    "ret": 0,
    "data": [
        {
            "name": "山东大学",
            "college_id": "A422",
            "address": "山东",
            "Type_college": [
                "普通本科",
                985,
                211,
                "双一流",
                "公办",
                "综合类"
            ]
        },{…},{…}],
“total”: 2 
}或(专科)
{
    "ret": 0,
    "data": [
        {
            "major_code": "410101",
            "major_name": "种子生产与经营",
            "big_type": "农林牧渔大类", #大类
            "major_year": "三年"
        },{…},{…}]，
“total”: 2 
}或(本科)
{
    "ret": 0,
    "data": [
        {
            "major_code": "120101",
            "major_name": "管理科学",
            "big_type": "管理学", #大类
            "small_type": "管理科学与工程类", #小类
            "major_year": "五年，四年",
            "academic": "理学，管理学"
        },{…},{…}]，
“total”: 2 
}
total为二表示系统中全部（不仅仅是这一页）有多少页数据
data 里面包含了所有的志愿信息列表

删除收藏院校/专业
请求消息
DELETE /api/students/delcollection HTTP/1.1

请求参数
{
	“action”: “del_college”, #或 del_major
	“major_set”: “本科”,# 当要删除专业时填写
	“major_id”: “xxxxx”,
	“college_id”: “xxxxxxx”,
	“account”: “12345678”
}

响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0
}

AI智能助手：
#请求问题答案
POST api/myai HTTP/1.1
Content-Type: application/json
{
“account”：“xxxxxx”，
“action”: “ai_action”,
"question":"xxxxxxx"
}
“action”字段固定为“ai_action”
"question"字段后写用户的问题
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”:0,
“result”: “xxxxxxxxx”
}
result 字段是AI助手给与回答的消息

查询信息：
#请求获取院校名称
请求消息
GET /api/students/getdata HTTP/1.1

请求参数
action为必填项，值为list_college
account为必填项，值为该账户，没做登录功能前默认12345678

响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0,
“college_name”: [‘清华大学’, ‘北京大学’…]
}
“college_name”列出全部院校的名称

#请求获取专业名称
请求消息
GET /api/students/getdata HTTP/1.1

请求参数
action为必填项，值为list_major
account为必填项，值为该账户，没做登录功能前默认12345678

响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0,
“major_name”: [‘信息管理’, ‘建筑学’…]
}
“major_name”列出全部专业的名称

登录系统：
#请求获取验证码
POST /api/students/givecode HTTP/1.1
Content-Type: application/json
{
"mail":"xxxxxxx"
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”:0,
“timeout”: 60, #验证码有效时间
“session_id”: “xxxxxx”
}
#注册
POST /api/students/signup HTTP/1.1
Content-Type: application/json
{
"account":"xxxxxx",
"password":"xxxxxx",
"mail":"xxxxxxxx",
"code":"xxxxxxx",
“session_id”: “xxxxxxxxx”
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{“ret”: 0}
{'ret': 1, 'msg': '该邮箱已被注册'}
{'ret': 1, 'msg': '该账户已存在'}
{'ret': 1, 'msg': '验证失败'}
{'ret': 1, 'msg': '验证码不存在'}
{'ret': 1, 'msg': '缺少会话ID'}


# 登录
请求消息
POST /api/students/signin HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
“account”: “xxxxxxxxx”, #这里可以是账户也可以是邮箱号，因此在注册的时候严格限制账号不可以含有@字符
“password”: “xxxxxxxx”
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0
}

#登出
请求消息
GET /api/students/signout HTTP/1.1

请求参数
无
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
“ret”: 0,
“msg”: “注销成功”
}

#找回密码
请求消息
POST /api/students/findpassword HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
"account":"xxxxxx",
"password":"xxxxxx", #注意这里的密码是新密码
"mail":"xxxxxxxx",
"code":"xxxxxxx",
“session_id”: “xxxxxxxxx”
}
响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{“ret”: 0}
找回密码和注册类似，注意，要先获取验证码
{'ret': 1, 'msg': '该邮箱已被注册'}
{'ret': 1, 'msg': '该账户已存在'}
{'ret': 1, 'msg': '验证失败'}
{'ret': 1, 'msg': '验证码已存在'}
{'ret': 1, 'msg': '缺少会话ID'}


添加考生信息：
请求消息
POST /api/students/grades HTTP/1.1
Content-Type: application/json

请求参数
http响应消息body中，数据以json格式存储
{
	“action”: “add_stu”,
	“stu_grd”: 688,
	“address”: “山东”,
	“subject”:[“化学”, “物理”, “生物”],
	“id”: “学生”,
	“ranking”:1652
	“account”: “12345678”
}
其中
action字段固定填写add_stu表示添加考生信息,将add_stu改为change_stu即可进行修改
stu_grd字段填写成绩
address字段填写考试所在省份
subject字段填写所选科目,非新高考省份列表后两个值填写为0
id字段表示用户的身份
ranking 字段表示考生位次
account 字段暂设置为12345678，后期加上登录之后再做修改

响应消息
HTTP/1.1 200 OK
Content-Type: application/json

响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”: 0,
	“gk_first”: 520,
	“gk_second”: 443,
	“gk_third”: 150,
	“gk_percentage”: 0.12,
}
其中
ret 为0表示成功
ranking 表示该分数所在的位次取值范围
gk_first
gk_second
gk_third 表示特招/一本，一段/二本，专科分数线
gk_percentage 表示该成绩在全省占前百分之多少

如果失败，格式如下：
{
	“ret”: 1,
	“msg”: “您填写省份或分数不存在”
}

{
	“ret”: 2,
	“msg”: “您所填写的位次与分数不匹配”,
	“re_ranking”: [1233,1455] 
}
其中re_ranking表示的是该分数下正确的位次区间
{
	“ret”: 3,
	“msg”: “您还没有登录”
}


请求生成志愿推荐：
请求消息
POST /api/students/recommend HTTP/1.1
Content-Type: application/json
请求参数
http响应消息body中，数据以json格式存储
{
	“action”: “rec_list_order”,
	“first”: “院校优先”,
	“like”: {
				“sort_by”: “综合排序”,
				“address”: “所有地区”,
				“type”: [“985”, “211”, “双一流”, “公办”, “综合类”, “提前批”],
				“major”:[],
				“set”: “本科”
}
	“account”: “12345678”
}
其中 
action 字段固定
first 表示为优先级
like 表示志愿意向, 其中如果选择院校优先，major字段不允许填写，默认为空
type 表示院校类型
account 为账户

响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
    "ret": 0,
    "college_major": [
        {
            "college_name": "浙江大学",
            "college_id": "10011",
            "address": "浙江",
            "type": ["普通本科", "公办", "985", "211", "双一流"],
            "plan": 157,
            "low_grades": 668,
            "low_ranking": 2155,
            "college_percent": 0.58,
            "majors": [
                {
                    "major_name": "社科实验班",
                    "major_id": "33",
                    "major_year": 4,
                    "major_pay": 5800,
                    "major_plan": 10,
                    "major_object": ["物理"],
                    "major_grades": 668,
                    "major_ranking": 2155,
                    "major_percent": 0.58
                },
                {
                    // 其他专业信息
                },
                ...
            ]
        },
        {
            // 其他院校信息
        },
        ...
    ]
}
在 “college_major”的值中存放着响应的大学信息：
	它的大体样子是这样的
“college_major”:[{每所大学的信息,’majors’:[每个专业的信息]}, …]
其中
大学信息中
“college_name”: 学校名称,
“college_id”: 院校代码,
“address”: 学校地址,
“type”:学校类型,
“plan”:今年计划招生人数, 
“low_grades”:去年最低分数线, 
“low_ranking”:去年最低位次, 
“college_percent”:被录取的概率
某一个专业的信息中
“major_name”: 专业名称, 
“major_id”: 专业代码, 
“major_year”:学制, 
“major_pay”:学费, 
“major_plan”:计划招收人数, 
“major_object”:限选科目（注：这是一个列表，以为可能有多个限选科目，如限选物理和化学）,
“major_grades”:去年最低分数线,
“major_ranking”:去年最低位次
“major_percent”:被该专业录取的概率

失败返回
{
	“ret”:1,
	“msg”: “出现不知名错误”
}

向“我的志愿表”中添加信息:
请求消息
POST /api/students/gkorder HTTP/1.1
Content-Type: application/json
请求参数
http响应消息body中，数据以json格式存储
{
	“action”: “add_order”,
	“data”:{
				“college_name”: “浙江大学”,
				“college_id”: “1233”,
				“major_name”: “社科实验班”,
				“major_id”: “33”
},
	“account”: “12345678”
}
其中action字段固定
data中存放着要添加的信息
account字段存放着账户

响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0
}

如果添加失败返回
{
	“ret”:1,
	“msg”: “该条志愿已经填写过”
}


申请获得“我的志愿表”中的信息

请求消息
GET /api/students/gkorder HTTP/1.1

请求参数
action为必填项，值为list_order
account为必填项，值为该账户，没做登录功能前默认12345678
pagesize 必填，分页的每页获取多少条记录
pagenum 必填，获取第几页的信息


响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0,
	“retlist”:[

{
	“order_id”:1,
					“college_name”: “浙江大学”,
					“college_id”: “1233”,
					“major_name”: “社科实验班”,
					“major_id”: “33”

},
{…},{…}…

],
	“total”:2
}
order_id表示第几条志愿
total为二表示系统中全部（不仅仅是这一页）有多少志愿
retlist 里面包含了所有的志愿信息列表


失败返回
{
	“ret”:1,
	“msg”: “无记录”
}


删除”我的志愿”中的记录
请求消息
DELETE /api/students/gkorder HTTP/1.1

请求参数
{
	“action”: “del_order”,
	“order_id”: 1,
	“account”: “12345678”
}

action固定
“order_id”表示要删除第几条记录
“account”表示账户

响应消息
HTTP/1.1 200 OK
Content-Type: application/json


响应内容
http响应消息body中，数据以json格式存储
如果获取消息成功，返回结果如下
{
	“ret”:0
}
失败返回
{
	“ret”:1,
	“msg”: “无法删除”
}
