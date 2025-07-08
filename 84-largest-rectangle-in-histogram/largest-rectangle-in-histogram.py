class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i, h in enumerate(heights):
            while stack and stack[-1][1] >= h:
                j, curr = stack.pop()
                pse = (j - stack[-1][0]) if stack else j + 1
                nse = i - j
                currArea = curr * (nse + pse - 1)
                maxArea = max(maxArea, currArea)
            
            stack.append((i, h))

        while stack:
            i, h = stack.pop()
            pse = (i - stack[-1][0]) if stack else i + 1
            nse = n - i
            currArea = h * (nse + pse - 1)
            maxArea = max(maxArea, currArea)

        return maxArea