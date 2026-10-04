class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.res = False

        def is_valid(board, word, i, j, word_idx):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            return True
        
        def dfs(i, j, curr, idx, visited):
            if len(curr) > len(word):
                return False
            
            if len(curr) == len(word) and "".join(curr) == word:
                self.res = True
                return True

            if is_valid(board, word, i, j, idx) and (i, j) not in visited:
                curr.append(board[i][j])
                visited.add((i, j))

                dfs(i+1, j, curr, idx+1, visited)
                dfs(i-1, j, curr, idx+1, visited)
                dfs(i, j+1, curr, idx+1, visited)
                dfs(i, j-1, curr, idx+1, visited)

                visited.remove((i, j))
                curr.pop()

            return False
        

        curr = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    dfs(i, j, [], 0, set())
                    if self.res == True:
                        return True

        return False