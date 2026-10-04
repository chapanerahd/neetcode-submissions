from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            
            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)
            
            return max(helper(i+1, j), 
            helper(i, j+1),
             helper(i+1, j+1)
             )
            
        return helper(0, 0)