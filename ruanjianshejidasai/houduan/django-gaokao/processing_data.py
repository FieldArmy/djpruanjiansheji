import pandas as pd
import re



def run():
    df1 = pd.read_excel('./20_22data/20-22data/专业选课限制目录.xlsx')
    df2 = pd.read_excel('./20_22data/20-22data/major_data.xlsx')
    df2['选科要求'] = 0

    data = {'college': [], 'major': []}

    for index, row in df2.iterrows():
        processing = df1[

                    df1['专业名称'].str[:3] == row['专业名称'][:3]

            ]

        if processing.empty:
            flag = '工程'
            if row['层次'] == '专科':
                df2.at[index, '选科要求'] = '不提科目要求'
            else:
                df2.at[index, '选科要求'] = '物理'
        else:
            df2.at[index, '选科要求'] = processing.iloc[0, processing.columns.get_loc('选科要求')]

    df2.to_excel('file.xlsx', index=False)
    print('创建完成')


if __name__ == '__main__':
    run()