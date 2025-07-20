class Solution(object):
    def sortedSquares(self, nums):
        output = []

        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                output.append(nums[l] ** 2)
                l += 1
            elif abs(nums[l]) <= abs(nums[r]):
                output.append(nums[r] ** 2)
                r -= 1
            
        return output[::-1]
        