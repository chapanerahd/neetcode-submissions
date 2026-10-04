class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        ans = curr_len = 0
        for num in unique_nums:
            if num - 1 not in unique_nums:
                while num in unique_nums:
                    curr_len += 1
                    num += 1
                ans = max(curr_len, ans)
                curr_len = 0
        return ans