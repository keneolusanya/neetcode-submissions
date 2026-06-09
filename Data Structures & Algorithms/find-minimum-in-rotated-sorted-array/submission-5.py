class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        res = 1000
        
        while l != r:
            m = int((l + r)/2)
            res = min(res, nums[m])
            if nums[r] > nums[l]:
                return min(res, nums[l])

            if nums[m] >= nums[l]:
                l = m + 1
                res = min(res, nums[l])
            else:
                r = m - 1
                res = min(res, nums[r])

        return res
            
            

        