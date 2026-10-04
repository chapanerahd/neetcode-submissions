class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node, visited):
            char = board[r][c]
            if char not in node.children:
                return
            
            if (r,c) in visited:
                return 
            
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None
            
            visited.add((r, c))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#':
                    dfs(nr, nc, next_node, visited)
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, set())

        return res