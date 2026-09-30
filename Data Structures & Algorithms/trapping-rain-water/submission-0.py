class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0] * len(height), [0] * len(height)

        left = 0
        for i in range(len(height)):
            maxLeft[i] = left
            left = max(left, height[i])
        
        right = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight[i] = right
            right = max(right, height[i])

        res = 0
        for i in range(len(height)):
            val = min(maxLeft[i], maxRight[i]) - height[i]
            if val > 0:
                res += val
        return res