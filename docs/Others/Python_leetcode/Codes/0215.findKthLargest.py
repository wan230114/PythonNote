import random


class Solution:
    def findKthLargest(self, nums, k):
        # 简便方法：
        # nums.sort()
        # return nums[-k]
        LEN_nums = len(nums)
        # print('\n【--start】', 'nums:', nums, 'LEN_nums:', LEN_nums, 'k:', k)
        i = 0 if LEN_nums == 1 else random.randint(0, len(nums)-1)
        seed = nums[i]
        nums0, nums1, nums2 = [], [], []
        for x in nums:
            if x == seed:
                nums0.append(x)
                nums1.append(x)
            elif x > seed:
                nums1.append(x)
            else:
                nums2.append(x)
        # print('i:', i, 'seed:', seed)
        LEN_num0 = len(nums0)
        LEN_num1 = len(nums1)
        # print(LEN_num0, nums0, LEN_num1, nums1)
        if LEN_num1 == k:
            return seed
        elif LEN_num1 > k:
            if LEN_num1 - LEN_num0 < k:
                return seed
            else:
                seed = self.findKthLargest(nums1, k)
        else:
            seed = self.findKthLargest(nums2, k-len(nums1))
        # print(seed, '已找到', nums1)
        return seed


# if __name__ == "__main__":
#     # k, L = 2, [3, 2, 1, 5, 6, 4]
#     k, L = 2, [2, 2, 1, 2, 3, 3, 4, 5]
#     # k, L = 20, [3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8,
#     #             2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6]
#     # k, L = 8, [3, 3, 3, 3, 3, 3, 3, 3, 3]
#     print('倒数第', k, '个数字', '正确的值是', sorted(L)[-k], '排序列表是', sorted(L))
#     result = Solution().findKthLargest(L, k)
#     print(result)

