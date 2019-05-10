class Solution:
    def getRow(self, rowIndex: int) -> list:
        if rowIndex == 0:
            return []
        
        pre = [1]
        for row_num in range(1, rowIndex):
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row)-1):
                row[j] = pre[j-1] + pre[j]
            pre = row
        return pre