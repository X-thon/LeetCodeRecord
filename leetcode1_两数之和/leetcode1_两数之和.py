from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums):
            temp = target - value
            if temp in d:
                return d.get(temp), index
            d.update({value:index})
        