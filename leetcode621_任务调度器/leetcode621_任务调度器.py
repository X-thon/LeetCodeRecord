from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0 or n < 0:
            return 0
        if n == 0:
            return len(tasks)
        counter = {}
        for i in tasks:
            counter[i] = counter.get(i, 0) + 1
        values = sorted(counter.values())
        max_num, max_len = values[-1], 0
        for i in values[::-1]:
            if i == max_num:
                max_len += 1
        return max((max_num-1)*(n+1)+max_len, len(tasks))