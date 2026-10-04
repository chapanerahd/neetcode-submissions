class Solution {
    public int maxProfit(int[] prices) {
        int[][] memo = new int[prices.length + 1][2];

        return getMaxProfit(prices, memo);
    }

    private int getMaxProfit(int[] prices, int[][] memo){
        for(int i = prices.length - 1; i >= 0; i--){
                memo[i][0] = Math.max(memo[i + 1][1] - prices[i], memo[i + 1][0]);
                memo[i][1] = Math.max(memo[i + 1][0] + prices[i], memo[i + 1][1]);
        }

        return memo[0][0];
    }
}

