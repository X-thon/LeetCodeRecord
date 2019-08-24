class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if word == "":
            return 0
        # 生成键盘字典
        sign, d = 0, dict()
        for i in keyboard:
            d[i] = sign
            sign += 1
        current, res = 0, 0
        for i in word:
            res += abs(d[i] - current)
            current = d[i]
        return res
        


solution = Solution()

print(solution.calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))