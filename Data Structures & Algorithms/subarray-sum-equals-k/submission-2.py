from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum : count
        ps = defaultdict(int)
        ps[0] = 1

        res = 0

        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum - k in ps:
                res += ps[curr_sum - k]
            ps[curr_sum] += 1
        
        return res


        