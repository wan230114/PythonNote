#%%
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
