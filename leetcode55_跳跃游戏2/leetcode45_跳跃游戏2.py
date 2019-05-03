from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        reach = 0
        next_location = nums[0]
        step = 0
        for i in range(0, len(nums)):
            next_location = max(i+nums[i], next_location)
            if next_location >= len(nums)-1: return step + 1
            if i == reach:
                step += 1
                reach = next_location
        return step
