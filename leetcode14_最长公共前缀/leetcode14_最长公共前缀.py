from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            j = 1
            while j < len(strs):
                if i == len(strs[j]) or c != strs[j][i]:
                    return strs[0][0:i]
                j += 1
        # 如果未在循环中跳出,那么最长公共前缀便是strs中第一个字符串了
        return strs[0]
