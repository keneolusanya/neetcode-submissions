class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        
        LIS = {
            len(nums) - 1 : 1
        }

        for i in reversed(range(len(nums) - 1)):
            check = [1]
            
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    check.append(1 + LIS[j])
            
            LIS[i] = max(check)  
        
        return max(LIS.values())
            