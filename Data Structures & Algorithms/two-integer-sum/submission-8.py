from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        my_dict = {}

        for i, num in enumerate(nums):
            if target - num in my_dict.keys():
                res.append(my_dict[target - num])
                res.append(i)
            else:
                my_dict[num] = i

        return res
        