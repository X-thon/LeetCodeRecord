from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        next = 0
        for i in range(0, len(nums)):
            if next >= len(nums)-1: return True
            if i == next:
                if nums[i] == 0: return False
                next = nums[i]
            if i + nums[i] > next:
                next = i + nums[i]
        return True
    