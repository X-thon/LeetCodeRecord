class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #检测特殊样例
        if s == None or len(s) == 0 or len(s) == 1:
            pass
        l = 0
        r = len(s) -1
        #使用头尾指针, 互换即可
        while l < r:
            temp = s[l]
            s[l], s[r] = s[r], temp
            l += 1
            r -= 1