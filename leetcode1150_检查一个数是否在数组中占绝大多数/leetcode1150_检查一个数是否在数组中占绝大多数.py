from collections import Counter
from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        c_nums = dict(Counter(nums))
        if c_nums.get(target, 0) > len(nums)//2:
            return True
        else:
            return False
            