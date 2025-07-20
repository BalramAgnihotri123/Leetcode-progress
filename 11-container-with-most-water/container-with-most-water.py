class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        maxWater = 0

        while l <= r:
            left = height[l]
            right = height[r]

            maxWater = max(maxWater, min(left, right) * (r - l))

            if left <= right:
                l += 1
            else:
                r -= 1

        return maxWater