class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        s = sum(A)

        if s % 3 != 0:
            return False
        sum_a = 0
        sum_b = 0
        i = 0
        j = len(A)-1
        while i < j:
            if sum_a != s//3 :
                sum_a += A[i]
                i += 1
            if sum_b != s//3 :
                sum_b += A[j]
                j -= 1           
            if sum_a == s//3 and sum_b == s//3:
                return True
        return False