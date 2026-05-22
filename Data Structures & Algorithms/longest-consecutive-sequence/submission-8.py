class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        final_res = 1
        my_set = set()

        for num in nums:
            my_set.add(num)

        for elem in my_set:
            if not elem - 1 in my_set:
                res = 1
                while(elem + 1 in my_set):
                    res += 1
                    elem += 1
                final_res = max(res, final_res)
        
        return final_res
