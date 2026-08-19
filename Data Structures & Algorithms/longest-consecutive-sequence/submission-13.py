class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:    
        mySet = set(nums)
        starts = []
        res = 1
        for n in nums:
            if n - 1 not in mySet:
                starts.append(n)

        for s in starts:
            currRes = 1
            while s + 1 in mySet:
                currRes += 1
                s += 1
            res = max(res, currRes)
        
        return res if len(nums) > 0 else 0
