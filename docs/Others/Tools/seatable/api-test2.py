
# %%

from datetime import datetime, timedelta
import pandas as pd
from seatable_api import Base, context

server_url = 'https://cloud.seatable.cn/'
api_token = '2c49121cf31c18b880f05d6b9e0900aa3c2bdf83'

base = Base(api_token, server_url)
# base = Base(context.api_token, context.server_url)
base.auth()

# %%

queryset = base.filter('项目总表')
df_xm = pd.DataFrame(queryset)

# %%
queryset = base.filter('项目子任务表', "今日任务排序!=''")
# for i in queryset:
#     print(i)
df_rw = pd.DataFrame(queryset)
df_rw["项目"] = df_rw["项目"].map(lambda x: x[0])
df_rw

# %%
df_all = pd.merge(df_xm, df_rw, left_on="_id",
                  right_on="项目", suffixes=["", "_rw"])
df_all = df_all[["项目类型", "项目名称", "项目状态", "名称", "今日任务排序", "任务描述"]]
df_all.columns
# %%
Date = (datetime.now() - timedelta(hours=8))  # 减去8小时
print("\n\n---\n#### ", Date.strftime(r"%Y-%m-%d 周") + "一二三四五六日"[Date.weekday()])
for xx1, df_tmp1 in df_all.groupby(["项目类型"]):
    print("- ", xx1)
    for xx2, df_tmp2 in df_tmp1.groupby(["项目名称"]):
        print(f'  - {xx2} 【stat: {df_tmp2.iloc[0]["项目状态"]}】')
        for idx in df_tmp2.index:
            stat = "[ ]" if df_tmp2.loc[idx, "今日任务排序"] == "0-完成" else "[x]"
            print(f'    - {stat} {df_tmp2.loc[idx, "名称"]}')
# %%

# queryset = base.filter('Table1', "age>18 and gender='male'")
# elder_queryset = queryset.filter("age > 70")
# for row in elder_queryset:
#     print(row)

# update_row_data = {'paid': True}
# updated_rows = elder_queryset.update(update_row_data)

# deleted_count = elder_queryset.delete()
