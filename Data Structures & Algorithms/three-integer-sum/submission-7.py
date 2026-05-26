class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) < 3):
            return []
        
        res = []
        nums = sorted(nums)

        print(nums)
        for i in range(0, len(nums) - 2):
            a = nums[i]
            l, r = i + 1, len(nums) - 1
            while l != r:
                x = nums[i] + nums[l] + nums[r] 
                if x == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif x < 0:
                    l += 1
                elif x > 0:
                    r -= 1

        #atp might have the exact array repeated but not the triplet
        # in any order repeated

        seen = set()
        temp = []

        for r in res:
            if tuple(r) not in seen:
                temp.append(r)
                seen.add(tuple(r))

        res = temp

        return res
            


