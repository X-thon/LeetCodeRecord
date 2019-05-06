"""
主要是去除除字母与数字之外的字符，并且注意题目条件，不区分大小写，则可以同一转为大写或小写
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        string = list()
        for i in range(0, len(s)):
            if "0" <= s[i] <= "9" or "a" <= s[i] <= "z":
                string.append(s[i])
        reverse_string = string[::-1]
        if reverse_string == string:
            return True
        else:
            return False
