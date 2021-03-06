class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                case1, case2 = s[l:r], s[l+1:r+1]
                return case1 == case1[::-1] or case2 == case2[::-1]
        return True