class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        nr, nc = len(matrix), len(matrix[0])
        fr = fc = 0
        ans = []
        while fr < nr and fc < nc:

            for c in range(fc, nc):
                ans.append(matrix[fr][c])
            
            fr += 1

            for r in range(fr, nr):
                ans.append(matrix[r][nc-1])
            
            nc -= 1

            if fr < nr:
                for c in range(nc-1, fc-1, -1):
                    ans.append(matrix[nr-1][c])
                
                nr -=1
            
            if fc < nc:
                for r in range(nr - 1, fr-1, -1):
                    ans.append(matrix[r][fc])
                fc += 1

        return ans



