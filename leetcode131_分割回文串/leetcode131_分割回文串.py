from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, tmp = [], []
        
        def dfs(s, tmp):
            if not s:
                res.append(tmp)
            # 因为下面要用到切片操作，用len(s) + 1做边界，即遍历到len(s)，切片时左闭右开(即到len(s)-1)，所以不会越界；
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    dfs(s[i:], tmp + [s[:i]])
        dfs(s, tmp)
        return res