class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ncol = len(matrix[0])
        nrow = len(matrix)
        self.prefix = [[0]*ncol for _ in range(nrow)]
        # first cell
        self.prefix[0][0] = matrix[0][0]
        # first row
        for i in range(1,ncol):
            self.prefix[0][i] = matrix[0][i] + self.prefix[0][i-1]
        # first column
        for i in range(1,nrow):
            self.prefix[i][0] = matrix[i][0] + self.prefix[i-1][0]
        # remaining matrix
        for i in range(1,nrow):
            for j in range(1,ncol):
                self.prefix[i][j] = (
                    matrix[i][j] + self.prefix[i][j-1] + self.prefix[i-1][j] - self.prefix[i-1][j-1]
                )
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]

        top = self.prefix[row1-1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1-1] if col1 > 0 else 0
        topleft = self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return total - top - left + topleft

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9],]
obj = NumMatrix(matrix)
print(obj.sumRegion(1,1,2,2))
print(obj.prefix)