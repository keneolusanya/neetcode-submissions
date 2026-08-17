class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l = 0, 0
        r = len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                temp = nums[i]
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
            
            if nums[i] == 2:
                temp = nums[i]
                nums[i] = nums[r]
                nums[r] = temp
                i -= 1
                r -= 1
            
            i += 1

    
    