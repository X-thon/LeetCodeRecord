class Solution:
    def longestDecomposition(self, text: str) -> int:
        head, tail = 0, len(text)-1
        th, tt = '', ''
        ans = 0
        while head < tail:
            # 字符串拼接的顺序很重要
            th =  th + text[head]
            tt = text[tail] + tt
            if th == tt:
                th, tt = '', ''
                ans += 2
            head += 1
            tail -= 1
        return ans + (1 if th or len(text) % 2 == 1 else 0)