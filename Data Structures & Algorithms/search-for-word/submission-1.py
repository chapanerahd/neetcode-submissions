class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def is_valid(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        
        def dfs(i, j, idx, visited):
            if idx == len(word):
                return True

            if not is_valid(i, j):
                return False

            if (i, j) in visited:
                return False

            if board[i][j] != word[idx]:
                return False

            visited.add((i, j))

            if dfs(i+1, j, idx+1, visited):
                return True
            if dfs(i-1, j, idx+1, visited):
                return True
            if dfs(i, j+1, idx+1, visited):
                return True
            if dfs(i, j-1, idx+1, visited):
                return True

            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, set()):
                        return True

        return False
