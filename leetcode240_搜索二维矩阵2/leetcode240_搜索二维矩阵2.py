class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        lrow, lcol = len(matrix), len(matrix[0])
        row, col = 0, lcol - 1
        while row <=lrow-1 and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False