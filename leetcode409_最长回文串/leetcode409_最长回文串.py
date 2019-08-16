# 直觉解法
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if s == "":
            return 0
        chars, flag = {}, False
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        res = 0
        for value in chars.values():
            if value % 2 == 0:
                res += value
            elif value > 1 and value % 2 != 0:
                res += value-1
                flag = True
            elif value == 1:
                flag = True
        if flag:
            res += 1
        return res