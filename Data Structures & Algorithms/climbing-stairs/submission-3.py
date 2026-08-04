class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        dp = [0] * (n + 1)
        for i in range(0, 3):
            dp[i] = i

        if n < 3:
            return dp[n]
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            if i == n:
                return dp[n]
