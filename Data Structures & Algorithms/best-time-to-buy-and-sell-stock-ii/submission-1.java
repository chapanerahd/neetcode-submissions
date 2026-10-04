class Solution {
    public int maxProfit(int[] prices) {
        int[][] memo = new int[prices.length][2];

        for(int i = 0; i < memo.length; i++){
            memo[i][0] = -1;
            memo[i][1] = -1;
        }

        return getMaxProfit(prices, 0, 0, memo);
    }

    private int getMaxProfit(int[] prices, int isBuy, int i, int[][] memo){
        if(i >= prices.length) return 0;

        if(memo[i][isBuy] != -1) return memo[i][isBuy];

        int result = 0;

        if(isBuy == 0){
            result = Math.max(getMaxProfit(prices, 1, i + 1, memo)  - prices[i], getMaxProfit(prices, 0, i + 1, memo));
        }
        else{
            result = Math.max(getMaxProfit(prices, 0, i + 1, memo) + prices[i], getMaxProfit(prices, 1, i + 1, memo));
        }

        memo[i][isBuy] = result;

        return result;
    }
}

