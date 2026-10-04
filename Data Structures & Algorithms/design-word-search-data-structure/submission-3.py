from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            
            if word[idx] == ".":
                for char in node.children:
                    if dfs(node.children[char], idx+1):
                        return True
                else:
                    return False

            elif word[idx] not in node.children:
                return False
            
            return dfs(node.children[word[idx]], idx+1)
            
            
        return dfs(curr, 0)







        
