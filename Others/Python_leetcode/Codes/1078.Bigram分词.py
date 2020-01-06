# %%
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
