from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if T == []:
            return []
        res = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            if stack == []:
                stack.append(i)
            elif T[i] > T[stack[len(stack)-1]]:
                while stack != [] and T[i] > T[stack[len(stack)-1]]:
                    index = stack.pop()
                    res[index] = i - index
                stack.append(i)
            else:
                stack.append(i)
        return res