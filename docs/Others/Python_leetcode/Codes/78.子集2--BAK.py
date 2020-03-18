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
        L_result = []  # 存储所有结果
        i_max_a = len(L_c) - i  # 表示最大索引a
        i_max_b = len(L_c) - 1  # 表示最大索引b
        L = np.arange(i)  # 临时存储结果的索引
        INDEX_i = -1  # 记录滑块位置
        while L[0] < i_max_a:
            if L[-1] < i_max_b:
                # print('\n-------->', L)
                L_result.append([L_c[i] for i in L])
                L[-1] += 1
            else:  # 到达右端
                # print('\nr', INDEX_i, L)
                # print('-------->', L)
                L_result.append([L_c[i] for i in L])

                # 1) 进行重建
                # print('重建中, 索引是',
                #       L[INDEX_i-1]+1,
                #       L[INDEX_i-1]+2-INDEX_i
                #       )
                L[INDEX_i-1:] = np.arange(
                    L[INDEX_i-1]+1,
                    L[INDEX_i-1]+2-INDEX_i
                )

                # 2) INDEX_i变化
                if L[-1] != i_max_b:
                    INDEX_i = -1
                else:
                    INDEX_i -= 1
                # print('c', INDEX_i, L)

        L_result.append([L_c[i] for i in L])
        print('\n', L_result)
        return L_result


# len(Solution().subsets([0, 1, 2, 3, 4, 5]))
# Solution().get_newL(1, [0, 1, 2, 3, 4])
# Solution().get_newL(2, [0, 1, 2, 3, 4])
# Solution().get_newL(3, [0, 1, 2, 3, 4, 5])  # 缺[0,3,4]
# Solution().get_newL(4, [0, 1, 2, 3, 4])
# Solution().get_newL(4, [0, 1, 2, 3, 4, 5])  # 缺[0,3,4,5]

# def select(self, L):
#     L_result = []
#     for i, x in enumerate(L):
#         for y in L[i+1:]:
#             L_result.append([x, y])
#             # print(x, y)
#     return L_result

# Solution().select([1, 2, 3, 4, 5])
