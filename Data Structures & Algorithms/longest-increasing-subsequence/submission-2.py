class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = {}
        def helper(i , prev):

            if i == len(nums):
                return 0

            if (i, prev) in dp:
                return dp[(i, prev)]
            
            if nums[i] > prev:
                dp[(i, prev)] = max(1 + helper(i+1, nums[i]), helper(i+1, prev))
                return dp[(i, prev)]

            dp[(i, prev)] = helper(i+1, prev)
            return dp[(i, prev)]
        
        return helper(0, -float('inf'))


            
