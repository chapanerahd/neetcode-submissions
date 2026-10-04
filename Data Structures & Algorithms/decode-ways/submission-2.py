from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def helper(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            res = helper(i+1)
            if i + 1 < len(s) and int(s[i: i+2]) <= 26:
                res += helper(i + 2)
            
            return res

        return helper(0)


