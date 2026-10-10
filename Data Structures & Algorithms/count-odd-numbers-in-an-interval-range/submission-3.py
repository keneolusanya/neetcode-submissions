class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return 1 if low % 2 == 1 else 0
        
        # return int((high - low) / 2) + 1
        return int((high - low) / 2) + 1