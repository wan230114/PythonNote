# 题目要求

模型评估是构建一个模型重要的一环，分类问题、排序问题、回归问题往往需要使用不同的指标进行评估。在这里我们将着重攻克常见的指标，如精确率，召回率，F1值，P-R曲线，ROC曲线和AUC。通过指标我们观察到欠拟合和过拟合时，该如何处理。

**算法视频课：** 快排、归并、堆排的实现，双指针/滑动窗口技术

## 算法刷题重点题型：（本周内完成）

双指针(题号：167)：  
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

快速选择、堆排序、归并排序（题号：215）：  
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

桶排序（题号：347）：  
https://leetcode.com/problems/top-k-frequent-elements/description/

双指针（题号：167）：  
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

滑动窗口（题号：209、438、76）：  
https://leetcode.com/problems/minimum-size-subarray-sum/  
https://leetcode.com/problems/find-all-anagrams-in-a-string/  
https://leetcode.com/problems/minimum-window-substring/  

（本次leetcode中涉及到排序的问题请同学们不要调用系统库函数去实现，尝试自己手动实现。）

## 算法刷题课后作业：（本周完成、不做打卡要求）

数组中重复的数字：https://www.nowcoder.com/practice/623a5ac0ea5b4e5f95552655361ae0a8

构建乘积数组：https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46

二维数组中的查找：https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e

打卡要求：（形式：文字，字数：150）说明对于不同的特征该如何进行特征工程？模型评估中不同的指标用在什么场景中？

打卡截止时间：2/2

## 学习笔记
### 快速排序

方法1：挖坑法

方法2：指针交换法

对应leetcode题号：

### 二叉堆

父节点小于等于子节点，不满足则交换

常用操作：
插入节点、删除节点

```
         1
       /   \
      3     2
     / \   / \
    6  5  7   8
   / \
  9  10

定义的二叉堆数组为：
[1,3,2,6,5,7,8,9,10]
```
