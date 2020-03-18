# %%
# import numpy as np


class Solution:
    def subsets(self, nums):
        L_result = [[]]
        S_c = nums.copy()
        for i in range(1, len(S_c)+1):
            L_result.extend(self.get_newL(i, S_c))
        print(L_result)
        return L_result

    def get_newL(self, i, L_c):
        """按照留的方法（就不用去了），还不错"""
        L_result = []  # 存储所有结果
        i_max_a = len(L_c) - i  # 表示最大索引a
        i_max_b = len(L_c) - 1  # 表示最大索引b
        L = list(range(i))  # 临时存储结果的索引
        INDEX_i = -1  # 记录滑块位置
        while L[0] < i_max_a:
            if L[-1] < i_max_b:
                L_result.append([L_c[i] for i in L])
                L[-1] += 1
            else:  # 到达右端
                L_result.append([L_c[i] for i in L])

                # 1) 进行重建
                L[INDEX_i-1:] = list(range(
                    L[INDEX_i-1]+1,
                    L[INDEX_i-1]+2-INDEX_i))
                # 2) INDEX_i变化
                if L[-1] != i_max_b:
                    INDEX_i = -1
                else:
                    INDEX_i -= 1
        L_result.append([L_c[i] for i in L])
        print('\n', L_result)
        return L_result
