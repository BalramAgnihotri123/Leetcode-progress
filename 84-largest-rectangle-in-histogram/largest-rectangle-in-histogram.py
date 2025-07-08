class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, height * width)
            
            stack.append(i)

        return maxArea