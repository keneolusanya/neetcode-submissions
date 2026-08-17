from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqs = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            freqs[n] += 1
        
        for key, val in freqs.items():
            buckets[val].append(key)

        for i in range(len(nums), 0, -1):
            for e in buckets[i]:
                res.append(e)
                if len(res) == k:
                    return res
    
        



