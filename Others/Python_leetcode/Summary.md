# 练习
## 0001.Two_Sum
### 题目：
```bash
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。  
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。  

示例:  
给定 nums = [2, 7, 11, 15], target = 9  
因为 nums[0] + nums[1] = 2 + 7 = 9  
所以返回 [0, 1]  
```
### 我的解法

#### 代码：0001.Two_Sum.py
```python
class Solution:
    def twoSum(self, nums, target):
        S = set(nums)
        for num in S:
            pre = target - num
            if num == pre:
                if nums.count(num) > 1:
                    index1 = nums.index(num)
                    return [index1, nums.index(num, index1+1)]
            elif pre in S:
                return [nums.index(num), nums.index(target - num)]


nums = [2, 2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))

nums = [2, 5, 5, 11]
target = 10
print(Solution().twoSum(nums, target))
```


<!-- <iframe src="/Others/Python_leetcode/0001.Two_Sum.html" name=iframe1 width='100%' height='500' frameborder='1' ></iframe> -->
#### 思路总结：
> 1. 不能重复利用元素——转换集合进行迭代
> 2. 依次遍历每一个元素，计算pre=tar-num
> 3. 判断pre是否与num相等，相等且存在两个以上这样的数结束循环，返回下标  
>    判断是否在集合中，若在结束循环，返回下标


## 0078.子集
### 题目：  
```bash
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。  

说明：解集不能包含重复的子集。  

示例：  
输入: nums = [1,2,3]  
输出: [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]
```
### 我的解法
#### 代码1：
```python
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


a = Solution().get_newL(4, [0, 1, 2, 3, 4])
print(a)
```
#### 代码2：
```python
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


a = Solution().get_newL(4, [0, 1, 2, 3, 4])
print(a)
```


#### 思路总结：
> 设定三个指标，控制循环发生。

![](img/2020-01-06-14-44-59.png)

## 0539.最小时间差
### 题目：
```bash
给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示。

示例 1：  
    输入: ["23:59","00:00"]  
    输出: 1  

备注:  
    列表中时间数在 2~20000 之间。  
    每个时间取值在 00:00~23:59 之间。  
```
### 我的解法
#### 代码：
```python
import datetime


class Solution:
    def findMinDifference(self, timePoints):
        S_timePoints = set(timePoints)
        if len(S_timePoints) != len(timePoints):
            return 0
        L_time = [datetime.datetime.strptime(x, "%H:%M")
                  for x in S_timePoints]
        S_time = set()
        for i, t1 in enumerate(L_time):
            for t2 in L_time[i+1:]:
                S_time.add(self.__getSeq__(t1, t2))
        return min(S_time)

    def __getSeq__(self, t1, t2):
        if t1 > t2:
            t2_next = t2 + datetime.timedelta(days=1)
            return min((t1 - t2).seconds//60,
                       (t2_next - t1).seconds//60)
        else:
            t1_next = t1 + datetime.timedelta(days=1)
            return min((t2 - t1).seconds//60,
                       (t1_next - t2).seconds//60)


Solution().findMinDifference(["23:59", "00:00"])
Solution().findMinDifference(["00:00", "00:00", "23:58"])
Solution().findMinDifference(["00:00", "00:01", "23:58"])
```
#### 思路总结
_

## 1078. Bigram 分词
### 题目
```bash
给出第一个词 first 和第二个词 second，
考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，
其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

 

示例 1：

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]
示例 2：

输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]
 

提示：

1 <= text.length <= 1000
text 由一些用空格分隔的单词组成，每个单词都由小写英文字母组成
1 <= first.length, second.length <= 10
first 和 second 由小写英文字母组成
```


### 我的解法
#### 代码
```python
class Solution:
    def findOcurrences(self, text, first, second):
        L_result = []
        L = text.split()
        imax = len(L) - 1
        i = 0
        while i < imax - 1:
            if L[i] == first and L[i+1] == second:
                L_result.append(L[i+2])
            i += 1
        return L_result


text, first, second = ("alice is aa good girl she is a good student",
                       "a",
                       "good")
text, first, second = ("we will we will rock you",
                       "we",
                       "will")
L_result = Solution().findOcurrences(text, first, second)
print(L_result)
```

#### 代码2
```python
class Solution:
    def findOcurrences(self, text, first, second):
        L_result = []
        L_text = text.split()
        text = ' ' + text
        while L_text:
            L_text = text.split(' %s %s ' % (first, second), 1)[1:]
            # print(text, L_text)
            if L_text:
                for x in L_text:
                    L_tmp = x.split()
                    if L_tmp:
                        L_result.append(L_tmp[0])
                text = ' ' + L_text[-1]
        return L_result


text, first, second = ("alice is aa good girl she is a good student",
                       "a",
                       "good")
text, first, second = ("we will we will rock you",
                       "we",
                       "will")
L_result = Solution().findOcurrences(text, first, second)
print(L_result)
```