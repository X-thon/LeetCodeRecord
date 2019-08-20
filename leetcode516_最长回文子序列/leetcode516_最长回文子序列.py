class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        len_s = len(s)
        dp = [[0 for col in range(len_s)] for row in range(len_s)]
        for i in range(len_s-1, -1, -1):
            dp[i][i] = 1
            j = i + 1
            while j < len_s:
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                j += 1
        return dp[0][len_s-1]


# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         if s == s[::-1]:
#             return len(s)

#         n = len(s)
#         dp = [0 for j in range(n)]
#         dp[n-1] = 1

#         for i in range(n-1, -1, -1):   # can actually start with n-2...
#             newdp = dp[:]
#             newdp[i] = 1
#             for j in range(i+1, n):
#                 if s[i] == s[j]:
#                     newdp[j] = 2 + dp[j-1]
#                 else:
#                     newdp[j] = max(dp[j], newdp[j-1])
#             dp = newdp
                    
#         return dp[n-1]