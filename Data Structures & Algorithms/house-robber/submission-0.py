from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache(None)
        def helper(n):
            if n == 0:
                return nums[0]
            if n == 1:
                return max(nums[0], nums[1])
            
            return max(helper(n-2) + nums[n], helper(n-1))
        
        return helper(len(nums)-1)
        