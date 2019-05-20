from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c2 = Counter(nums2)
        ans = []
        for i in nums1:
            if i in c2 and c2[i] > 0:
                ans.append(i)
                c2[i] -= 1
        return ans