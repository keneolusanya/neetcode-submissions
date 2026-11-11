class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1] * len(triangle)] * len(triangle)

        for i in range(len(triangle) - 1, -1, -1):
            if i == len(triangle) - 1:
                for x in range(i + 1):
                    dp[i][x] = triangle[i][x]
            else:
                for y in range(i + 1):
                    dp[i][y] = triangle[i][y] + min(dp[i + 1][y], dp[i + 1][y + 1])

        return dp[0][0]


