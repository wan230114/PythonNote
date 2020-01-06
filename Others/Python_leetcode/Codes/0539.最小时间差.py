"""
给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并已分钟数表示。

示例 1：
输入: ["23:59","00:00"]
输出: 1

备注:
列表中时间数在 2~20000 之间。
每个时间取值在 00:00~23:59 之间。
"""
# %%
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
