from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps = defaultdict(int)
        ps[0] = 1
        res = 0
        for i in range(1, len(nums) + 1):
            currSum = sum(nums[0:i])
            diff = currSum - k
            if diff in ps:
                res += ps[diff]
            ps[currSum] += 1
        
        return res
            