
# %%

# pip3 install seatable-api
import pandas as pd
from seatable_api import Base, context

# server_url = context.server_url or 'https://cloud.seatable.cn'
# api_token = context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'
# context.server_url or 'https://cloud.seatable.cn'

server_url = 'http://jun-seatable.com'
api_token = '414b45b3a070cd9af84a8e9c4fb22ae9152eae8a'

# context.api_token or 'c3c75dca2c369849455a39f4436147639cf02b2d'


base = Base(api_token, server_url)
base.auth()

# %%


queryset = base.filter('项目信息表', "物种-种属='人'")
for i in queryset:
    print(i)
pd.DataFrame(queryset)

# %%

# queryset = base.filter('Table1', "age>18 and gender='male'")
# elder_queryset = queryset.filter("age > 70")
# for row in elder_queryset:
#     print(row)

# update_row_data = {'paid': True}
# updated_rows = elder_queryset.update(update_row_data)

# deleted_count = elder_queryset.delete()
