class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find out smallest element and track index
        l, r = 0, len(nums) - 1
        res = 1000
        minIndex = 0

        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < res:
                    res = nums[l]
                    minIndex = l
                    break
            
            m = (l + r) // 2
            if nums[m] < res:
                res = nums[m]
                minIndex = m

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        # list 1 binary search
        l, r = 0, minIndex - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1

            elif nums[m] > target:
                r = m - 1

            else:
                return m

        # list 2 binary search
        l, r = minIndex, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1

            elif nums[m] > target:
                r = m - 1

            else:
                return m

        return -1


       