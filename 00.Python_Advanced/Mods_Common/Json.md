
简单示例：
```python
import json
# 引入json模块
L = [1,2,3,4]
# 创建一个列表L。

L_a_str = json.dumps(L)  # --> str
# 使用dumps()函数，将列表a转换为json格式的字符串，赋值给L_a_str。
print(L_a_str)
# 打印L_a_str。
print(type(L_a_str))
# 打印L_a_str的数据类型。

L_b = json.loads(L_a_str)
# 使用loads()函数，将json格式的字符串L_a_str转为列表，赋值给L_b。
print(L_b)
# 打印L_b。
print(type(L_b)) 
# 打印L_b的数据类型。
```