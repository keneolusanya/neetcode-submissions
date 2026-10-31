class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for n in nums1:
            curr = -1
            check = False
            for inner in nums2:
                if inner == n:
                    check = True
                if check and inner > n:
                    curr = inner
                    break
            res.append(curr)

        return res





