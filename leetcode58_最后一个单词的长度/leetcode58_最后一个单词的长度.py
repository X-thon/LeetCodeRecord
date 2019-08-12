class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s == '':
            return 0
        l = s.rstrip(" ").split(" ")
        return len(l[-1])