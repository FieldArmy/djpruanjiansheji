import os
import django
import pandas as pd
import json

# 配置环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gk_back.settings")
django.setup()

from common.models import College, Admissions, MajorType01, MajorType02


def register_college():
    queryset = College.objects.all()
    # 若表为空
    if not queryset.exists():
        # 读取 Excel 文件
        df1 = pd.read_excel('./20_22data/20-22data/college_data.xlsx', sheet_name='Sheet2')
        df2 = pd.read_excel('./20_22data/20-22data/college_data.xlsx', sheet_name='Sheet1')
        df3 = pd.read_excel('./20_22data/20-22data/院校分类.xlsx')
        data_list = []
        for index, row in df1.iterrows():
            # 筛选出与该院校匹配的另外一个表中的数据
            extend_data = df2[df2['学校名称'] == row['院校名称']]
            # 不返回none返回空对象
            if extend_data.empty:
                print(f"没有找到该院校匹配的数据（{row['院校名称']}）")
                return
            first_data = extend_data.iloc[0]
            # 院校类型定义为json格式
            type_list = []
            type_list.append(first_data['学校性质'])
            for column in df3.columns:
                if row['院校名称'] in df3[column].values:
                    type_list.append(column)
            # type_list = json.dumps(type_list)
            college = College(
                name=first_data['学校名称'],
                id=row['院校代码'],
                address=first_data['省份'],
                plan=10,
                Type_college=type_list,
                college_ranking=index + 1
            )
            data_list.append(college)
        # 批量插入数据
        College.objects.bulk_create(data_list)
        print('创建完成！\n')

    else:
        print('该表已存在数据，无法导入')


def register_admissions():
    queryset = Admissions.objects.all()
    # 若表为空
    if not queryset.exists():
        data_list = []
        # 读取 Excel 文件
        data_2020 = pd.read_excel('./20_22data/20-22data/2020data/2020data.xlsx')
        data_2021 = pd.read_excel('./20_22data/20-22data/2021data/2021data.xlsx')
        data_2022 = pd.read_excel('./20_22data/20-22data/2022data/2022data.xlsx')
        grades_2020 = pd.read_excel('./20_22data/20-22data/2020data/2020年夏季高考文化成绩一分一段表.xlsx')
        grades_2021 = pd.read_excel('./20_22data/20-22data/2021data/2021年夏季高考文化成绩一分一段表.xlsx')
        grades_2022 = pd.read_excel('./20_22data/20-22data/2022data/2022年夏季高考文化成绩一分一段表.xlsx')
        plan_2023 = pd.read_excel('./20_22data/20-22data/major_data.xlsx')
        college_foreignkey = College.objects
        # 按照今年的招生计划录入数据
        for index, row in plan_2023.iterrows():
            admissions_dict = {}
            admissions_dict['provinces_name'] = '山东'
            # 院校外键
            try:
                admissions_dict['college'] = college_foreignkey.get(id=row['院校代码'])
            except:
                a = row['院校代码']
                print(f'未找到该院校{a}')
                return
            admissions_dict['major_id'] = row['专业代码']
            admissions_dict['major_name'] = row['专业名称']
            admissions_dict['major_ranking'] = 0
            admissions_dict['major_set'] = row['层次']
            if row['层次'] == '本科':
                admissions_dict['major_year'] = 4
            else:
                admissions_dict['major_year'] = 3
            admissions_dict['major_pay'] = 5500
            admissions_dict['major_num'] = row['计划人数']

            # 算出近三年最低录取位次和分数
            d20 = data_2020[
                ((data_2020['院校代码'] == row['院校代码']) | (data_2020['院校名称'] == row['院校名称'])) & (
                            (data_2020['专业代码'] == row['专业代码']) | (data_2020['专业名称'] == row['专业名称']))]
            if d20.empty:
                admissions_dict['Three_year_grades'] = 0
                admissions_dict['Three_year_ranking'] = 0
            else:
                admissions_dict['Three_year_ranking'] = d20.iloc[0, d20.columns.get_loc('位次')]
                g20 = grades_2020[(grades_2020['累计人数'] >= d20.iloc[0, d20.columns.get_loc('位次')])
                                  & ((grades_2020['累计人数'] - grades_2020['本段人数'])
                                     <= d20.iloc[0, d20.columns.get_loc('位次')])]
                if g20.empty:
                    admissions_dict['Three_year_grades'] = 0
                else:
                    admissions_dict['Three_year_grades'] = g20.iloc[0, g20.columns.get_loc('分数段')]
            ###########################################################################################################
            d21 = data_2021[((data_2021['院校代码'] == row['院校代码']) | (data_2021['院校名称'] == row['院校名称'])) & (
                            (data_2021['专业代码'] == row['专业代码']) | (data_2021['专业名称'] == row['专业名称']))]
            if d21.empty:
                admissions_dict['Two_year_grades'] = 0
                admissions_dict['Two_year_ranking'] = 0
            else:
                admissions_dict['Two_year_ranking'] = d21.iloc[0, d21.columns.get_loc('位次')]
                g21 = grades_2021[(grades_2021['累计人数'] >= d21.iloc[0, d21.columns.get_loc('位次')])
                                  & (grades_2021['累计人数'] - grades_2021['本段人数']
                                     <= d21.iloc[0, d21.columns.get_loc('位次')])]
                if g21.empty:
                    admissions_dict['Two_year_grades'] = 0
                else:
                    admissions_dict['Two_year_grades'] = g21.iloc[0, g21.columns.get_loc('分数段')]
            ###########################################################################################################
            d22 = data_2022[((data_2022['院校代码'] == row['院校代码']) | (data_2022['院校名称'] == row['院校名称'])) & (
                            (data_2022['专业代码'] == row['专业代码']) | (data_2022['专业名称'] == row['专业名称']))]
            if d22.empty:
                admissions_dict['One_year_grades'] = 0
                admissions_dict['One_year_ranking'] = 0
            else:
                admissions_dict['One_year_ranking'] = d22.iloc[0, d22.columns.get_loc('位次')]
                g22 = grades_2022[(grades_2022['累计人数'] >= d22.iloc[0, d22.columns.get_loc('位次')])
                                  & (grades_2022['累计人数'] - grades_2022['本段人数']
                                     <= d22.iloc[0, d22.columns.get_loc('位次')])]
                if g22.empty:
                    admissions_dict['One_year_grades'] = 0
                else:
                    admissions_dict['One_year_grades'] = g22.iloc[0, g22.columns.get_loc('分数段')]

            admissions_dict['wuli_class'] = False
            admissions_dict['huaxue_class'] = False
            admissions_dict['shengwu_class'] = False
            admissions_dict['dili_class'] = False
            admissions_dict['lishi_class'] = False
            admissions_dict['zhengzhi_class'] = False
            admissions_dict['flag_class'] = False
            if '/' in row['选科要求']:
                admissions_dict['flag_class'] = True
            if '物理' in row['选科要求']:
                admissions_dict['wuli_class'] = True
            if '思想政治' in row['选科要求']:
                admissions_dict['zhengzhi_class'] = True
            if '化学' in row['选科要求']:
                admissions_dict['huaxue_class'] = True
            if '生物' in row['选科要求']:
                admissions_dict['shengwu_class'] = True
            if '地理' in row['选科要求']:
                admissions_dict['dili_class'] = True
            if '历史' in row['选科要求']:
                admissions_dict['lishi_class'] = True
            admissions = Admissions(
                i_index=index,
                provinces_name=admissions_dict['provinces_name'],
                college=admissions_dict['college'],
                major_id=admissions_dict['major_id'],
                major_name=admissions_dict['major_name'],
                major_ranking=admissions_dict['major_ranking'],
                major_set=admissions_dict['major_set'],
                major_year=admissions_dict['major_year'],
                major_pay=admissions_dict['major_pay'],
                major_num=admissions_dict['major_num'],
                One_year_greads=admissions_dict['One_year_grades'],
                One_year_ranking=admissions_dict['One_year_ranking'],
                Two_year_grades=admissions_dict['Two_year_grades'],
                Two_year_ranking=admissions_dict['Two_year_ranking'],
                Three_year_grades=admissions_dict['Three_year_grades'],
                Three_year_ranking=admissions_dict['Three_year_ranking'],
                wuli_class=admissions_dict['wuli_class'],
                huaxue_class=admissions_dict['huaxue_class'],
                shengwu_class=admissions_dict['shengwu_class'],
                dili_class=admissions_dict['dili_class'],
                lishi_class=admissions_dict['lishi_class'],
                zhengzhi_class=admissions_dict['zhengzhi_class'],
                flag_class=admissions_dict['flag_class']

            )
            data_list.append(admissions)

        print(len(data_list))
        Admissions.objects.bulk_create(data_list)
        print('创建完成！\n')

    else:
        print('该表已存在数据，无法导入')


def major_type():
    queryset = MajorType01.objects.all()
    queryset2 = MajorType02.objects.all()
    # 若表为空
    if not queryset.exists() and not queryset2.exists():
        # 读取 Excel 文件
        df1 = pd.read_excel('./20_22data/20-22data/major_type.xlsx')
        df2 = pd.read_excel('./20_22data/20-22data/major_type_2.xlsx')
        data_list01 = []
        data_list02 = []
        for index, row in df1.iterrows():
            major01 = MajorType01(
                major_code=row['专业代码'],
                major_name=row['专业名称'],
                big_type=row['门类'],
                small_type=row['专业类'],
                major_year=row['修业年限'],
                academic=row['学位授予门类']
            )
            data_list01.append(major01)
        # 批量插入数据
        MajorType01.objects.bulk_create(data_list01)
        for index, row in df2.iterrows():
            major02 = MajorType02(
                major_code=row['专业代码'],
                major_name=row['专业名称'],
                big_type=row['专业类别'],
                major_year=row['修业年限']
            )
            data_list02.append(major02)
        # 批量插入数据
        MajorType02.objects.bulk_create(data_list02)
        print('创建完成！\n')

    else:
        print('该表已存在数据，无法导入')


if __name__ == "__main__":
    print('请选择你要创建的注册的数据库（1、College；2、Admissions；3、MajorType）\n')
    check_num = input()
    if check_num == '1':
        register_college()
    elif check_num == '2':
        register_admissions()
    elif check_num == '3':
        major_type()
