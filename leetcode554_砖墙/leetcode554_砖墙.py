from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        d = {}
        for row in wall:
            gap_location = 0
            for i in range(len(row) - 1):
                gap_location += row[i]
                d[gap_location] = d.get(gap_location, 0) + 1
        res = 0
        for i in d.values():
            if i > res:
                res = i
        return len(wall) - res