class Solution(object):
    def trap(self, height):
        n = len(height)
        if n <= 2:
            return 0

        maxLeft, maxRight = height[0], height[n - 1]
        l, r = 1, n - 2

        water = 0
        while l <= r:
            if maxLeft <= maxRight:
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l]
                l+=1
            else:
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r]
                r-=1

        return water
