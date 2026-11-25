from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        res = 0
       
        currSum = 0
        for n in nums:
            currSum += n

            if currSum - k in sums:
                res += sums[currSum - k]
            
            sums[currSum] += 1

        return res