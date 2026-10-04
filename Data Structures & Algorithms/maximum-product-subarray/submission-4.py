class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0


        curr_max = curr_min = ans = nums[0]
        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(curr_max * num, num)
            curr_min = min(curr_min * num, num)
            ans = max(curr_max, ans)
        return ans
