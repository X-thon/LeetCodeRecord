# 本体使用库函数的话解法将变得十分简单，且一定程度上失去了意义

# class Solution:
#     def sortedSquares(self, A: list) -> list:
#         for i in range(len(A)):
#             A[i] = A[i] * A[i]
#         A.sort()
#         return A

# class Solution:
#     def sortedSquares(self, A):
#         return sorted([x ** 2 for x in A])

class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans