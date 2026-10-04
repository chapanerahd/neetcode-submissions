class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        left_subarray, right_subarray = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums) - 1):
            left_subarray[i + 1] = left_subarray[i] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            right_subarray[i] = right_subarray[i + 1] * nums[i + 1]

        print(left_subarray)
        print(right_subarray)
        for i in range(len(nums)):
            ans[i] = left_subarray[i] * right_subarray[i]
        
        return ans