class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prefix = [1]
        right_prefix = [1]
        for i in range(len(nums) - 1, -1, -1):
            right_prefix.append(right_prefix[-1] * nums[i])
        
        right_prefix = right_prefix[::-1]
        left = 1
        ans = []
        for i in range(len(nums)):
            ans.append(left * right_prefix[i + 1])
            left *= nums[i]
        
        return ans
