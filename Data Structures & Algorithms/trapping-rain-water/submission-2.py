class Solution:
    def trap(self, height: List[int]) -> int:
        # maxLeft, maxRight = [0] * len(height), [0] * len(height)

        # left = 0
        # for i in range(len(height)):
        #     maxLeft[i] = left
        #     left = max(left, height[i])
        
        # right = 0
        # for i in range(len(height) - 1, -1, -1):
        #     maxRight[i] = right
        #     right = max(right, height[i])
        # res = 0
        # for i in range(len(height)):
        #         res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        # return res

        leftMax, rightMax = 0, 0
        res = 0
        l, r = 0, len(height) - 1
        while l <= r:
            if leftMax < rightMax:
                res += max(leftMax - height[l], 0)
                print("REs, ", res)
                leftMax = max(leftMax, height[l])
                print("leftamx, ", leftMax)
                l += 1
            else:
                res += max(rightMax - height[r], 0)
                print("REs, ", res)
                rightMax = max(rightMax, height[r])
                print("rightMax,", rightMax)
                r -= 1
                
        return res















