class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows_to_update = set()
        cols_to_update = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows_to_update.add(r)
                    cols_to_update.add(c)

        for r in rows_to_update:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        
        for c in cols_to_update:
            for r in range(len(matrix)):
                matrix[r][c] = 0
    

