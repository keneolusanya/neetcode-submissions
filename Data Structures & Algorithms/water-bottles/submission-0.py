class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        drank = numBottles

        while empty >= numExchange:
            empty -= numExchange - 1
            drank += 1

        return drank



        

        

