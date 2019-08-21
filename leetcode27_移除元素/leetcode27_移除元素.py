from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n, i = len(nums), 0
        while i < n:
            # 每次修改都会缩短n，所以最后直接返回n即可
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i += 1
        return n