from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(houses):
            @lru_cache(None)
            def helper(n):
                if n == 0:
                    return houses[0]

                if n == 1:
                    return max(houses[0], houses[1])

                return max(
                    helper(n - 1),
                    helper(n - 2) + houses[n]
                )

            return helper(len(houses) - 1)

        return max(
            solve(nums[:-1]),  # Exclude the last house
            solve(nums[1:])    # Exclude the first house
        )
