class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0] * (len(triangle) + 1)] * (len(triangle) + 1)

        for i in range(len(triangle) - 1, -1, -1):
                for x in range(i + 1):
                    dp[i][x] = triangle[i][x] + min(dp[i + 1][x], dp[i + 1][x + 1])

        return dp[0][0]


