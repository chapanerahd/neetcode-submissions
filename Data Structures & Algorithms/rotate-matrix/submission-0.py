class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        nrow, ncol = len(matrix), len(matrix[0])
        for i in range(nrow):
            for j in range(i, ncol):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(nrow):
            for j in range(ncol // 2):
                matrix[i][j], matrix[i][ncol-1-j] = matrix[i][ncol-1-j], matrix[i][j]

