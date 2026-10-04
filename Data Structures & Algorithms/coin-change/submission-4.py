class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(idx, target):

            if target == 0:
                return 0

            if target in dp:
                return dp[target]
            
            ans = float('inf')
            for i in range(idx, len(coins)):
                if target - coins[i] >= 0:
                    ans = min(1 + helper(idx, target-coins[i]), ans)
            
            dp[target] = ans
            return ans
        
        res = helper(0, amount)
        return -1 if res == float('inf') else res