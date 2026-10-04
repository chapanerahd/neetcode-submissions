class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # start = [float(inf)] * len(cost)
        # start[0] = 0
        # start[1] = 0

        total = 0
        dp = [None] * len(cost)
        def helper(i):
            nonlocal total
            if i >= len(cost):
                return 0
            
            if dp[i]:
                return dp[i]
            
            dp[i] = min(cost[i] + helper(i+1), cost[i] + helper(i+2))
            return dp[i]

        return min(helper(0), helper(1))

        

            
