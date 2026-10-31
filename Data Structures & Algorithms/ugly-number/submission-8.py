class Solution:
    def isUgly(self, n: int) -> bool:
        # it's only prime factors are two three and five
        while n % 5 == 0:
            n /= 5
        
        while n % 3 == 0:
            n /= 3
        
        while n % 2 == 0:
            n /= 2

        return n == 1
