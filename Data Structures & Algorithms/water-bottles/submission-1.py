class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = drank = numBottles

        while empty >= numExchange:
            empty -= numExchange - 1
            drank += 1

        return drank



        

        

