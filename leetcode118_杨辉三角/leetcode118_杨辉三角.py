class Solution:
    def generate(self, numRows: int) -> list:
        triangle = []
        if numRows == 0:
            return triangle
        
        for row_count in range(numRows):
            #因为迭代从0到numRows-1
            row = [None for _ in range(row_count+1)]
            row[0], row[-1] = 1, 1
            #不知道row[0]=row[-1]=1这种赋值方式是否会产生指向同一个值的引用

            #range(1, len(row)-1)便是从row的第二个数到倒数第二个数，即不包括边界
            for j in range(1, len(row)-1):
                row[j] = triangle[row_count-1][j-1] + triangle[row_count-1][j]
            triangle.append(row)

        return triangle