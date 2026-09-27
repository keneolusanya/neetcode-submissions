import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        count = 0
        while n > 0:
            curr = math.floor(math.log(n, 2))
            n -= 2 ** curr
            res += 1

        return res