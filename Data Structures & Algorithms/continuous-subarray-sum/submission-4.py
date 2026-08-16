from itertools import accumulate

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref = {0:-1}

        curSum = 0
        for i, n in enumerate(nums):
            curSum += n
            rem = curSum % k
            if rem in pref and i - pref[rem] >= 2:
                return True
            elif rem not in pref:
                pref[rem] = i

        return False
            