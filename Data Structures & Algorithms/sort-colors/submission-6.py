class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freqs = {}
        for n in nums:
            freqs[n] = 1 + freqs.get(n, 0)
        
        i = 0
        if 0 in freqs:
            while freqs[0] > 0:
                nums[i] = 0
                freqs[0] -= 1
                i += 1
        if 1 in freqs:
            while freqs[1] > 0:
                nums[i] = 1
                freqs[1] -= 1
                i += 1
        if 2 in freqs:
            while freqs[2] > 0:
                nums[i] = 2
                freqs[2] -= 1
                i += 1

    
    