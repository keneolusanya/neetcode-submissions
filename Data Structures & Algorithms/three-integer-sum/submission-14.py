from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        
        for a in range(len(nums)):
            currNums = sorted(nums[a + 1: len(nums)])
            l = 0
            r = len(currNums) - 1
            target = 0 - nums[a]
            while l < r:
                if currNums[l] + currNums[r] < target:
                    l += 1
                elif currNums[l] + currNums[r] > target:
                    r -= 1
                else:
                    ans = tuple(sorted((nums[a],currNums[l], currNums[r])))
                    if ans not in seen:
                        res.append([nums[a],currNums[l], currNums[r]])
                        seen.add(ans)
                    l += 1
                    r -= 1

        return res
