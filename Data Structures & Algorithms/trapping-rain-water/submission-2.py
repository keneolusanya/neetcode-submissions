class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [None] * len(height)
        maxRight = [None] * len(height)

        currMax = 0
        for i in range(len(height)):
            maxLeft[i] = currMax
            currMax = max(currMax, height[i])

        currMax = 0
        for i in reversed(range(len(height))):
            maxRight[i] = currMax
            currMax = max(currMax, height[i])

        res = 0
        for i in range(len(height)):
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            if diff > 0:
                res += diff
        
        return res