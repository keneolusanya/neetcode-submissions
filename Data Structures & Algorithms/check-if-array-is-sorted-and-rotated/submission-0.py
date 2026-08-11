class Solution:
    def check(self, nums: List[int]) -> bool:
        # compare the ends
        # if end is greater than start, loop through and check
        # if end is smaller than start, check backwards from end and forward
        # from start until they meet
        if nums[0] < nums[-1]:
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
            return True
        else:
            l, r = 0, len(nums) - 1
            while True:
                if nums[r] < nums[r - 1]:
                    break
                else:
                    r -= 1
            while True:
                if nums[l] > nums[l + 1]:
                    break
                else:
                    l += 1
            return r - l <= 1
