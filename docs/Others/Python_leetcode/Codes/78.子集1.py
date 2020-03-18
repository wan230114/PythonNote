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

import itertools


class Solution:
    def subsets(self, nums):
        L_result = [[]]
        S_c = nums.copy()
        for i in range(1, len(S_c)+1):
            L_result.extend(self.get_newL(i, S_c))
        print(L_result)
        return L_result

    def get_newL(self, i, L_c):
        return [i for i in itertools.combinations(L_c, i)]


a = Solution().get_newL(4, [0, 1, 2, 3, 4])  # 缺0134
print(a)
