from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(n):
            if n < 1:
                return 0

            if n == 1:
                return 1

            if n == 2:
                return 2
            
            return helper(n-1) + helper(n-2)

        return helper(n)