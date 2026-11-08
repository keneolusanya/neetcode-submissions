class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1
        setNums = set(nums)
        for n in range(1, len(nums) + 1):
            if n not in setNums:
                return n
            
        return n + 1
