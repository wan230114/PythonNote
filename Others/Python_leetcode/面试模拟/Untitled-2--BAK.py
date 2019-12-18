# %%
"""
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

    说明：解集不能包含重复的子集。

    示例：
    输入: nums = [1,2,3]
    输出:
    [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
    ]
"""

import numpy as np


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
        i_max = len(L_c)-1
        L_i = np.arange(i)  # 存储结果的索引
        # L_i_c = L_i.copy()
        L_result = []
        INDEX_a = 0
        INDEX_b = 0
        while L_i[0] <= i_max - i:
            # print('\n--start-- [L_i[0]:%s  i_max-i:%s]' %
            #       (L_i[0], i_max-i), L_i_c)
            if L_i[-1] < i_max:
                print('append1', L_i)
                L_result.append([L_c[i] for i in L_i])
                L_i[-1] += 1
            else:
                print('append2', L_i)
                L_result.append([L_c[i] for i in L_i])
                print('\nr', INDEX_b, L_i)  # , L_i_c)
                if L_i[INDEX_b-1]+1 != L_i[INDEX_b]:
                    INDEX_b -= 1
                L_i[INDEX_b-1] += 1
                L_i[INDEX_b] = L_i[INDEX_b-1] + 1
                print('c', INDEX_b, L_i)  # , L_i_c)
                # L_i[:] = L_i_c[:]
                # if L_i_c[INDEX_b-1] > i_max:
                if L_i[INDEX_b-1] == L_i[0]:
                    INDEX_a += 1
                    INDEX_b = 0
                    L_i = np.arange(i)+INDEX_a
                    # print('重建', L_i)
            # print('---end--- [L_i[0]:%s  i_max-i:%s]' %
            #       (L_i[0], i_max-i), L_i_c)
        L_result.append([L_c[i] for i in L_i])
        # print(L_result)
        return L_result


# len(Solution().subsets([1, 2, 3, 4, 5]))
# Solution().get_newL(2, [0, 1, 2, 3])
Solution().get_newL(3, [0, 1, 2, 3, 4])
# Solution().get_newL(4, [0, 1, 2, 3, 4])

# def select(self, L):
#     L_result = []
#     for i, x in enumerate(L):
#         for y in L[i+1:]:
#             L_result.append([x, y])
#             # print(x, y)
#     return L_result

# Solution().select([1, 2, 3, 4, 5])
