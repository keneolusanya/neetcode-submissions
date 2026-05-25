class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        mySet = set()
        for num in nums:
            mySet.add(num)

        starts = []
        for num in mySet:
            if num + 1 in mySet:
                starts.append(num)

        res = 1
        for start in starts:
            maxNum = 1
            while start + 1 in mySet:
                maxNum += 1
                start += 1
            if (maxNum > res):
                res = maxNum

        return res
 
    # if i + 1 is in the set