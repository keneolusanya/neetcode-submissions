class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, i):
            if i < len(nums):
                dfs(subset.copy(), i + 1)
                if i == len(nums) - 1:
                    res.append(subset.copy())
                subset.append(nums[i])
                dfs(subset.copy(), i + 1)
                if i == len(nums) - 1:
                    res.append(subset.copy())
                
        dfs([], 0)
        return res