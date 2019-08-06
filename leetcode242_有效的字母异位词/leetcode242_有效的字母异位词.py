from collections import Counter

# 解法1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果长度不一致，直接返回false
        if len(s) != len(t):
            return False
        else:
            res = {}
            for i in s:
                if i in res:
                    res[i] += 1
                else:
                    res[i] = 1
            for i in t:
                if i in res:
                    res[i] -= 1
                else:
                    return False
            for i in res:
                if res[i] != 0:
                    return False
            return True

# 解法2
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)