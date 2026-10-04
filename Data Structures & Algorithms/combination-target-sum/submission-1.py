class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = []
        def dfs(idx, curr, remaining):

            if idx == len(nums):
                return
            
            if remaining < 0:
                return

            if remaining == 0:
                ans.append(curr.copy())
                return 
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(i, curr, remaining - nums[i])
                curr.pop()
        
        dfs(0, [], target)
        return ans
