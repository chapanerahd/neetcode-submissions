class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj_list = {}
        indegrees = {}
        for word in words:
            for char in word:
                if char not in adj_list:
                    adj_list[char] = set()
                    indegrees[char] = 0


        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            min_word_len = min(len(word1), len(word2))
            if word1[:min_word_len] == word2[:min_word_len] and len(word1) > len(word2):
                return ""
            
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in adj_list[char1]:
                        adj_list[char1].add(char2)
                        indegrees[char2] += 1
                    break
        
        queue = deque([char for char in indegrees if indegrees[char] == 0])
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for neigh in adj_list[curr]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    queue.append(neigh)
        
        if len(res) != len(indegrees):
            return ""

        return "".join(res)