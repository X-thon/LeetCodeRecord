from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count = 0
        l = len(bits)
        if bits[l-1] == 1: return False
        else:
            for i in range(l-2, -1, -1):
                if bits[i] == 1:
                    count += 1
                else:
                    break
            if count % 2== 0:
                return True
            else:
                return False