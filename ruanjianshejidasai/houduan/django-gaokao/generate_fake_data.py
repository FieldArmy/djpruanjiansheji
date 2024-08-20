import os
import django
import json
import random

# 配置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gk_back.settings")
django.setup()
from common.models import Students, College, Admissions, Gkorder


def generate_fake_data():
    # 生成学生信息
    for i in range(100):
        account = f"student{i}"
        stu_grd = random.randint(500, 750)
        address = random.choice(['山东'])
        sid = random.choice(["xuesheng", "jiazhang", "laoshi"])
        sel_class = random.sample(['物理', '化学', '生物', '政治', '地理', '历史'], 3)
        sel_class = json.dumps(sel_class)
        ranking = 1000000 // stu_grd

        Students.objects.create(account=account, stu_grd=stu_grd, address=address, sid=sid, ranking=ranking,
                                sel_class=sel_class)

    # 生成院校信息
    for i in range(50):
        name = f"院校{i}"
        college_id = f"{i}"
        address = random.choice(["北京", "上海", "广州", "深圳", "成都", "武汉"])
        plan = random.randint(10, 100)
        college_ranking = random.randint(1, 100)

        # 生成院校类型
        type_college = []
        for j in range(1, 7):
            if random.random() < 0.5:
                type_college.append(j)
        type_college = json.dumps(type_college)

        College.objects.create(name=name, id=college_id, address=address, plan=plan,
                               Type_college=type_college, college_ranking=college_ranking)

    # 生成志愿推荐表数据
    for i in range(100):
        provinces_name = random.choice(['山东'])
        college = random.choice(College.objects.all())
        major_id = f"{i}"
        major_name = f"专业{i}"
        major_ranking = random.randint(1, 100)
        major_set = random.choice(["本科", "专科"])
        major_year = random.randint(3, 5)
        major_pay = random.randint(3000, 10000)
        major_num = random.randint(1, 10)
        one_year_grades = random.randint(500, 750)
        one_year_ranking = random.randint(1, 2000)
        two_year_grades = random.randint(500, 750)
        two_year_ranking = random.randint(1, 2000)
        three_year_grades = random.randint(500, 750)
        three_year_ranking = random.randint(1, 2000)

        wuli_class = random.choice([True, False])
        huaxue_class = random.choice([True, False])
        shengwu_class = random.choice([True, False])
        dili_class = random.choice([True, False])
        lishi_class = random.choice([True, False])
        zhengzhi_class = random.choice([True, False])

        Admissions.objects.create(provinces_name=provinces_name, college=college, major_id=major_id,
                                  major_name=major_name, major_ranking=major_ranking, major_set=major_set,
                                  major_year=major_year, major_pay=major_pay, major_num=major_num,
                                  One_year_greads=one_year_grades, One_year_ranking=one_year_ranking,
                                  Two_year_grades=two_year_grades, Two_year_ranking=two_year_ranking,
                                  Three_year_grades=three_year_grades, Three_year_ranking=three_year_ranking,
                                  wuli_class=wuli_class, huaxue_class=huaxue_class, shengwu_class=shengwu_class,
                                  dili_class=dili_class, lishi_class=lishi_class, zhengzhi_class=zhengzhi_class)

    print("Fake data generated successfully!")


if __name__ == "__main__":
    generate_fake_data()
