class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fw_arr = [1]
        bw_arr = [1]

        pfw = 1
        for i in range(len(nums) - 1):
            pfw *= nums[i]
            fw_arr.append(pfw)
        print(fw_arr)

        pbw = 1
        for i in range(len(nums) - 1, 0, -1):
            pbw *= nums[i]
            bw_arr.append(pbw)
        bw_arr = list(reversed(bw_arr)) 
        
        print(bw_arr)
        res = []
        for i in range(len(nums)):
            res.append(fw_arr[i] * bw_arr[i])

        return res

         

        
        



