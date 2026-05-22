class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = []
        final_res = 0

        for num in nums:
            if (not num - 1 in nums) and (num + 1 in nums):
                arr.append(num)

        if nums:
            final_res = 1

        for elem in arr:
            res = 1
            while(elem + 1 in nums):
                res += 1
                elem += 1
            final_res = max(final_res, res)

        return final_res