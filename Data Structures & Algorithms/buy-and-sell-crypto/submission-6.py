class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            print(prices[l])
            print(prices[r])
            print()
            # as long as l is less than right check rights
            if prices[l] <= prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return profit