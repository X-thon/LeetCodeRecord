from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        1 : 仍然为1
        -1 : 1转0
        0 : 仍然为0
        2 : 0转1
        """
        # 标记
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = self.check(board, i, j)
        # 刷新
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = 1 if board[i][j] == 1 or board[i][j] == 2 else 0


    def check(self, board: List[List[int]], i: int, j:int):
        count = 0
        top = max(i-1, 0)
        bottom = max(i+1, len(board)-1)
        left = max(j-1, 0)
        right = max(j+1, len(board[i])-1)
        for k in range(top, bottom+1):
            for v in range(left, right+1):
                if board[k][v] == 1 or board[k][v] == -1:
                    count += 1

        res = (1 if count == 3 or count == 4 else -1) if board[i][j] == 1 else (2 if count == 3 else 0)
        return res