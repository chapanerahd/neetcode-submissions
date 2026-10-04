class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curr_sum = max_sum = -float('inf')
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum < nums[i]:
                curr_sum = nums[i]
            max_sum = max(curr_sum, max_sum)
        
        return max_sum