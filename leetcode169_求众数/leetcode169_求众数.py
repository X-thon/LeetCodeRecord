from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         if not nums:
#             return
        
#         d = {}
#         for i in nums:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#         #return max(d, key=lambda x: d[x])
#         return max(d.keys(), key=d.get)

# Boyer-Moore 投票算法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, candidate = 0, None
        for num in nums:
            if count == 0 :
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate