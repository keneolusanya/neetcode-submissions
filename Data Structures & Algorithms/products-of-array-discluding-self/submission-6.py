class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = []

        curr = 1
        for n in nums:
            l.append(curr)
            curr *= n 
        
        curr = 1
        for n in reversed(nums):
            r.append(curr)
            curr *= n
        r.reverse()
        
        prod = []
        for i in range(len(nums)):
            prod.append(l[i] * r[i])

        return prod
