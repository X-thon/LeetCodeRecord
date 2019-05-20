from typing import List

# class Solution:
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         a = set(nums1)
#         b = set(nums2)
#         return list(a & b)

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))