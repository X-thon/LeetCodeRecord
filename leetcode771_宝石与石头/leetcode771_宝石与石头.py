class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([i for i in S if i in J])
        #return sum(S.count(i) for i in J)