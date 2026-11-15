class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Set<Integer> coinsSet = new HashSet<>();
        for (int coin: coins) {
            coinsSet.add(coin);
        }
        
        dp[0] = 0;

        for (int i = 1; i < dp.length; i++) {
            if (coinsSet.contains(i)) {
                dp[i] = 1;
            } else {
                int res = amount + 1;
                for (int coin: coins) {
                    if (coin < i && (1 + dp[i - coin]) < res) {
                        res = 1 + dp[i - coin];
                    }
                }
                dp[i] = res;
            }
        }
        
        if (dp[amount] == amount + 1) {
            return -1;
        }
        return dp[amount];
    }
}
