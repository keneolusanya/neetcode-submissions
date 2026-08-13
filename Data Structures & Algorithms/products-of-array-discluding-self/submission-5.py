class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [None] * len(nums)

        for i in range(len(nums) - 1):
            left.append(left[i] * nums[i])

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right[i] = 1

            else:
                right[i] = (right[i + 1] * nums[i + 1])
        
        res = []
        for i in range(len(nums)):
            res.append(left[i] * right[i])

        return res