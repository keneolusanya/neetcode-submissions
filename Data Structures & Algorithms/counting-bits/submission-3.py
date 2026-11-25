class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]
        offsets = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512}
        off = None
        for i in range(1, n + 1):
            if i in offsets:
                off = i
            dp.append(1 + dp[i - off])
        
        return dp
                

            
