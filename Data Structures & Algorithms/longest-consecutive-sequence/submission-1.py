class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            curr = num
            curr_lcs = 1
            if curr - 1 not in nums:
                while curr + 1 in nums:
                    curr += 1
                    curr_lcs += 1
            ans = max(curr_lcs, ans)
        
        return ans
