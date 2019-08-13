class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 1000000007
        dp = [[None for col in range(1001)] for row in range(31)]
        min_num = min(f, target)
        for i in range(1, min_num+1):
            dp[1][i] = 1
        targetMax = d * f
        for i in range(2, d+1):
            for j in range(i, targetMax+1):
                k = 1
                while j - k >= 0 and k <= f:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-k]) % mod
                    k += 1
        return dp[d][target]
