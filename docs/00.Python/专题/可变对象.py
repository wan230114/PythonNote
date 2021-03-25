# %%
# 已知：让 L 变量绑定的列表为 空列表， 有以下两种方式
L = [1, 2, 3, 4]
L.clear()  # 方式1
print(L)

L = [1, 2, 3, 4]
L = []     # 方式2
print(L)

# %%
# 创建一个列表  [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
L = []
L_tmp = []
for x in range(10):
    L_tmp.append(x)
    if x == 4:
        L.append(L_tmp)
        L_tmp.clear()  # 方式1
        # L_tmp = []   # 方式2
    elif x == 9:
        L.append(L_tmp)

print(L)
