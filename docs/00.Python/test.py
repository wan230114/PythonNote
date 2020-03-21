# - 排序规则
#   - 先按照书籍编号降序排序
#   - 再按照书名正序排序
#   - 再按照年份降序排序

# 书籍的编号
number = {
    "Robinson Crusoe": "B",
    "The Old Man and the Sea": "A",
    "The Little Prince": "C",
    "Secret garden": "A",
    "Thorn bird": "A"
}

# 年份，书籍，销售额
data_text = """2017,126,Robinson Crusoe
2017,110,The Old Man and the Sea
2017,152,The Little Prince
2017,98,Secret garden
2017,89,Thorn bird
2018,116,Robinson Crusoe
2018,98,The Old Man and the Sea
2018,176,The Little Prince
2018,79,Secret garden
2018,90,Thorn bird
2019,122,Robinson Crusoe
2019,102,The Old Man and the Sea
2019,187,The Little Prince
2019,102,Secret garden
2019,103,Thorn bird"""

Datas = [x.split(',') for x in data_text.splitlines()]
# 对数据进行排序
result = sorted(Datas, key=lambda x: (ord(number[x[2]])*-1,
                                      x[2], int(x[0])*-1))
# 结果的打印
for x in result:
    print(number[x[2]], *x, sep='\t')
