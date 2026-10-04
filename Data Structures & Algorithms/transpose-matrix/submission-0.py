class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        nr, nc = len(matrix), len(matrix[0])
        res = [[0] * nr for _ in range(nc)]
        for c in range(nc):
            for r in range(nr):
                res[c][r] = matrix[r][c]
        return res