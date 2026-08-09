class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []
        diff = 0
        # first k numbers
        for i in range(k):
            diff += abs(x - arr[i])

        minDiff = 10000000
        l = 0
        r = k - 1

        while True:
            if diff < minDiff:
                res = arr[l:r + 1]
                minDiff = diff

            diff -= abs(x - arr[l])
            l += 1
            r += 1
            print(r)
            if r == len(arr):
                break
            diff += abs(x - arr[r])

        return res