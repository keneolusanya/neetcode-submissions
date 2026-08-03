from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = len(nums) // 2
        myMap = defaultdict(int)

        for n in nums:
            if myMap[n] == a:
                return n
            myMap[n] += 1
        
            
