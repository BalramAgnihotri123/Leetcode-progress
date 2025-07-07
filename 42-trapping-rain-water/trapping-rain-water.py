class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 1, n - 2
        maxLeft, maxRight = height[0], height[n - 1]
        water = 0

        while l <= r:
            if maxLeft <= maxRight:
                if maxLeft > height[l]:
                    water += maxLeft - height[l]
                else:
                    maxLeft = height[l]
                l += 1
            else:
                if maxRight > height[r]:
                    water += maxRight - height[r]
                else:
                    maxRight = height[r]
                r -= 1

        return water