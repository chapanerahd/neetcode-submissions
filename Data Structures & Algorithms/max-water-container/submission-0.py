class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        curr_sum = ans = 0
        left, right = 0, len(heights) - 1
        while left < right:
            curr_sum = min(heights[left], heights[right]) * (right - left)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            ans = max(curr_sum, ans)
        return ans
