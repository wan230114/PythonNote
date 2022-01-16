"""
https://leetcode-cn.com/problems/maximal-rectangle/
思路：
* 遍历每一个矩阵的左上角顶点
* 判断该点右下角可能的矩阵
* 记录出现过
"""
# %%
class Solution:
    def maximalRectangle(self, matrix):
        """: List[List[str]]) -> int"""
        # step0 先计算数据的维数
        if not matrix:
            return 0
        self.matrix = matrix
        self.x = len(matrix)
        self.y = len(matrix[0])
        MAX = 0
        # step1 找左上角顶点
        for xi in range(self.x):
            for yi in range(self.y):
                if matrix[xi][yi] == "1":
                    # print(f"\nfind comput area. {xi} {yi}")
                    # 计算该点涉及的最大面积
                    area = self.comput_area(xi, yi)
                    if area > MAX:
                        MAX = area
                        # print("MAX", MAX)
        return MAX

    def comput_area(self, xi, yi):
        # xi, yi = 0,0
        xii, yii = xi, yi
        # 先在单个元素组内横向判断
        while yii < self.y:
            if self.matrix[xi][yii] == "0":
                yii -= 1
                break
            yii += 1
        else:
            yii -= 1
        while xii < self.x:
            if self.matrix[xii][yi] == "0":
                xii -= 1
                break
            xii += 1
        else:
            xii -= 1
        MAX_area, MAX_x, MAX_y = 0, xi, yi
        for x in range(xi, xii+1):
            for y in range(yi, yii+1):
                # print(f"[test]({xii}, {yii}) ({x},{y}): {self.matrix[x][y]}")
                if self.matrix[x][y] == "0":
                    yii = y - 1
                    break
                area = (x - xi + 1) * (y - yi + 1)
                if area > MAX_area:
                    MAX_area, MAX_x, MAX_y = area, x, y
        # print(f"({xi},{yi}) --> ({MAX_x},{MAX_y}): {MAX_area}")
        # print(*self.matrix, sep="\n")
        return MAX_area


# Solution().maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
# 输出：6

# Solution().maximalRectangle(matrix = [["0","0","0","0","0","0","1"],["0","0","0","0","1","1","1"],["1","1","1","1","1","1","1"],["0","0","0","1","1","1","1"]])
# 输出：9

# Solution().maximalRectangle(matrix=[["1", "0", "1", "0", "0"], [
#     "1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
# 输出：6

# Solution().maximalRectangle(matrix=[["1", "0", "1", "1", "1"], ["0", "1", "0", "1", "0"], [
#     "1", "1", "0", "1", "1"], ["1", "1", "0", "1", "1"], ["0", "1", "1", "1", "1"]])
# 输出：6

Solution().maximalRectangle(matrix=[["1", "0", "1", "1", "0", "1"], ["1", "1", "1", "1", "1", "1"], [
    "0", "1", "1", "0", "1", "1"], ["1", "1", "1", "0", "1", "0"], ["0", "1", "1", "1", "1", "1"], ["1", "1", "0", "1", "1", "1"]])
# 输出：8

# Solution().maximalRectangle(matrix = [])
# # 输出：0

# Solution().maximalRectangle(matrix = [["0"]])
# # 输出：0

# Solution().maximalRectangle(matrix = [["1"]])
# # 输出：1

# Solution().maximalRectangle(matrix = [["0","0"]])
# # 输出：0
