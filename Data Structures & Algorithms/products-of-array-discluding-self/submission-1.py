class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        pf = []
        sf = []
        res = []

        for i, num in enumerate(nums):
            pd = 1
            curr_index = i
            while(curr_index > 0):
                pd *= nums[curr_index - 1]
                curr_index -= 1
            pf.append(pd)

        for i, num in enumerate(nums):
            pd = 1
            curr_index = len(nums) - i - 1
            while(curr_index < len(nums) - 1):
                pd *= nums[curr_index + 1]
                curr_index += 1
            sf.append(pd)
        
        sf.reverse()
        for i in range(len(nums)):
            res.append(pf[i] * sf[i])
            
        return res
            

        