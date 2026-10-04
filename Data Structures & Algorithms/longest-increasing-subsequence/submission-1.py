from functools import lru_cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def helper(i , prev):

            if i == len(nums):
                return 0
            
            if nums[i] > prev:
                return max(1 + helper(i+1, nums[i]), helper(i+1, prev))

            return helper(i+1, prev)
        
        return helper(0, -float('inf'))


            
