from django.db import models


# Create your models here.

# 学生
class Students(models.Model):
    objects = models.Manager()
    # 账户
    account = models.CharField(max_length=200, primary_key=True)
    # 学生分数
    stu_grd = models.IntegerField(null=True)
    # 选课
    sel_class = models.TextField(null=True)
    # 所在省份
    address = models.CharField(max_length=20, null=True)
    # 身份
    id_choices = (
        ('xuesheng', '学生'),
        ('jiazhang', '家长'),
        ('laoshi', '老师'),
    )

    sid = models.CharField(max_length=10, choices=id_choices, null=True)
    # 位次
    ranking = models.IntegerField(null=True)
    # 密码
    password = models.CharField(max_length=200)
    # e_mail
    mail = models.CharField(max_length=100, unique=True)
    # 是否将信息填写完整
    check_data = models.BooleanField(default=False)


# 院校
class College(models.Model):
    objects = models.Manager()
    # 名称
    name = models.CharField(max_length=100)
    # 代码
    id = models.CharField(max_length=100, primary_key=True)
    # 地址
    address = models.CharField(max_length=100)
    # 计划招生
    plan = models.IntegerField()
    # 院校类型
    Type_college = models.JSONField()
    # 院校排名
    college_ranking = models.IntegerField()


# 志愿推荐表
class Admissions(models.Model):
    objects = models.Manager()
    i_index = models.IntegerField(primary_key=True)
    # 所在招生省份
    provinces_name = models.CharField(max_length=100)
    # 院校外键
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    # 专业代码
    major_id = models.CharField(max_length=100)
    # 专业名称
    major_name = models.CharField(max_length=100)
    # 专业排名
    major_ranking = models.IntegerField()
    # 专业是本科还是专科
    major_set = models.CharField(max_length=10)
    # 学制
    major_year = models.IntegerField()
    # 学费
    major_pay = models.IntegerField()
    # 计划招生人数
    major_num = models.IntegerField()
    # 去年最低分
    One_year_greads = models.IntegerField()
    # 去年最低位次
    One_year_ranking = models.IntegerField()
    # 前年最低分
    Two_year_grades = models.IntegerField()
    # 前年最低位次
    Two_year_ranking = models.IntegerField()
    # 大前年最低分
    Three_year_grades = models.IntegerField()
    # 大前年最低位次
    Three_year_ranking = models.IntegerField()
    # 限选科目
    wuli_class = models.BooleanField(default=False)
    huaxue_class = models.BooleanField(default=False)
    shengwu_class = models.BooleanField(default=False)
    dili_class = models.BooleanField(default=False)
    lishi_class = models.BooleanField(default=False)
    zhengzhi_class = models.BooleanField(default=False)
    # 判断选课是不是’/‘
    flag_class = models.BooleanField(default=False)
    # 方便遍历
    class_map = {
        1: 'wuli_class',
        2: 'huaxue_class',
        3: 'shengwu_class',
        4: 'dili_class',
        5: 'lishi_class',
        6: 'zhengzhi_class',
    }

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['provinces_name', 'college_id', 'major_id'], name='unique_constraint_name')
        ]


# 志愿收藏表
class Gkorder(models.Model):
    objects = models.Manager()
    # 单设一个主键
    id = models.AutoField(primary_key=True)
    # 志愿序号
    Gk_id = models.IntegerField()
    # 账户
    account = models.ForeignKey(Students, on_delete=models.CASCADE)
    # 院校代码
    college_id = models.CharField(max_length=100)
    # 专业代码
    major_id = models.CharField(max_length=100)
    # 院校名称
    college_name = models.CharField(max_length=100)
    # 专业名称
    major_name = models.CharField(max_length=100)
    # 专科还是本科
    major_set = models.CharField(max_length=4)

    class Meta:
        # 这里我把Gk_id从unique里去掉了，方便重复填写比对
        constraints = [
            models.UniqueConstraint(fields=['account', 'college_id', 'major_id'], name='unique_order')
        ]


# 本科专业
class MajorType01(models.Model):
    objects = models.Manager()
    # 专业代码
    major_code = models.CharField(max_length=32)
    # 专业名称
    major_name = models.CharField(max_length=32)
    # 大类
    big_type = models.CharField(max_length=32)
    # 小类
    small_type = models.CharField(max_length=32)
    # 学制
    major_year = models.CharField(max_length=32)
    # 授予学位
    academic = models.CharField(max_length=32)


# 专科专业
class MajorType02(models.Model):
    objects = models.Manager()
    # 专业代码
    major_code = models.CharField(max_length=32)
    # 专业名称
    major_name = models.CharField(max_length=32)
    # 大类
    big_type = models.CharField(max_length=32)
    # 学制
    major_year = models.CharField(max_length=32)


# 咨询师信息
class Teachers(models.Model):
    objects = models.Manager()
    # 专业层次
    major_set = models.CharField(max_length=10)
    # 专业门类
    major_type = models.CharField(max_length=32)
    # 姓名
    name = models.CharField(max_length=10)
    # 性别
    sex = models.CharField(max_length=2)
    # 年龄
    age = models.IntegerField()
    # 账户
    account = models.CharField(max_length=32, unique=True)
    # 密码
    password = models.CharField(max_length=32)
    # 个人简介
    text = models.TextField()
    # 联系电话
    phonenumber = models.CharField(max_length=48)
    # 联系邮箱
    mail = models.CharField(max_length=48)
    # 被咨询次数
    advice_num = models.IntegerField(default=0)


# 咨询信息
class Advice(models.Model):
    objects = models.Manager()
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    # 问题
    question = models.TextField()
    # 回答
    advice = models.TextField(default='暂未收到回复')
    # 询问时间
    time = models.DateTimeField(auto_now_add=True)


# 反馈问题
class Issues(models.Model):
    objects = models.Manager()
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    # 问题
    issue = models.TextField()
    # 反馈时间
    time = models.DateTimeField(auto_now_add=True)


# 管理员
class Manager(models.Model):
    objects = models.Manager()
    # 账户
    account = models.CharField(max_length=32, unique=True)
    # 密码
    password = models.CharField(max_length=32)


# 收藏院校
class CollectCollege(models.Model):
    objects = models.Manager()
    # 院校
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    # 学生账号
    account = models.ForeignKey(Students, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['college', 'account'], name='unique_constraint_name0')
        ]


# 收藏专业,本科
class CollectMajor01(models.Model):
    objects = models.Manager()
    # 学生账号
    account = models.ForeignKey(Students, on_delete=models.CASCADE)
    # 本科专业
    major = models.ForeignKey(MajorType01, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['major', 'account'], name='unique_constraint_name1')
        ]


# 收藏专业, 专科
class CollectMajor02(models.Model):
    objects = models.Manager()
    # 学生账号
    account = models.ForeignKey(Students, on_delete=models.CASCADE)
    # 专科专业
    major = models.ForeignKey(MajorType02, on_delete=models.CASCADE)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['major', 'account'], name='unique_constraint_name2')
        ]