class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = [] # decreasing from bottom to top; area = top * len(stack)
        res = 0
        for i in range(len(heights)):
            height = heights[i]
            index = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                res = max(res, h * (i - index))
            stack.append((index, height))
        
        while stack:
            index, h = stack.pop()
            res = max(res, h * (len(heights) - index))
        return res
            

        