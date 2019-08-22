from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = dict()
        for i in S:
            d[i] = S.rfind(i)
        index, res = d[S[0]], []
        for i, c in enumerate(S):
            if d[c] > index:
                index = d[c]
            if i == index:
                res.append(index + 1 - sum(res))
        return res