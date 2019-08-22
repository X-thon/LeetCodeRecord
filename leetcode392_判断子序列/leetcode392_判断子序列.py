# 不使用库函数的普通解法
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if s == "":
#             return True
#         te = -1
#         for i in range(len(s)):
#             tt = te
#             for j in range(tt+1, len(t)):
#                 if s[i] == t[j]:
#                     tt = j
#                     break
#                 else:
#                     continue
#             if tt == te:
#                 return False
#             else:
#                 te = tt
#         return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = -1
        for i in s:
          index = t.find(i, index+1)
          if index == -1:
            return False
        return True