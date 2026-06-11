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

        # from that index you now have two lists (sorted) you can split
        list1 = nums[0:minIndex]
        list2 = nums[minIndex:]

        # list 1 binary search
        l, r = 0, len(list1) - 1

        while l <= r:
            m = (l + r) // 2
            if list1[m] < target:
                l = m + 1

            elif list1[m] > target:
                r = m - 1

            else:
                return m

        # list 2 binary search
        l, r = 0, len(list2) - 1

        while l <= r:
            m = (l + r) // 2
            if list2[m] < target:
                l = m + 1

            elif list2[m] > target:
                r = m - 1

            else:
                return m + len(list1)

        return -1


       