from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
            if counts[num] > (n / 2):
                return num
        

