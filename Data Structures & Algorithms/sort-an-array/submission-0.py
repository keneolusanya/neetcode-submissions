class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for _ in range(len(nums) - 1):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
    
        return nums