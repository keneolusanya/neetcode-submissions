from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        res = []

        for n in nums:
            freqs[n] += 1

        while k > 0:    
            maxFreq = 0
            maxNum = None
            for key, val in freqs.items():
                if val > maxFreq:
                    maxFreq = val
                    maxNum = key
            res.append(maxNum)
            freqs.pop(maxNum)
            k -= 1

        return res


