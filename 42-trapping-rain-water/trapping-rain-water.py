class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLefts, maxRights = [0] * n, [0] * n
        stack = []

        maxLefts[0] = height[0]
        for i in range(1, n):
            maxLefts[i] = max(maxLefts[i-1], height[i])

        maxRights[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            maxRights[i] = max(maxRights[i+1], height[i])
        print(maxLefts, maxRights)
        water = 0
        for i, h in enumerate(height):
            currWater = min(maxLefts[i], maxRights[i]) - h
            water += currWater if currWater >= 0 else 0

        return water