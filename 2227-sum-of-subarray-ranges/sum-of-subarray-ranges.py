class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        nge, pge, nse, pse = [0] * n, [0] * n, [0] * n, [0] * n
        stack1, stack2 = [], []

        for i in range(n - 1, -1, -1):
            curr = nums[i]
            while stack1 and nums[stack1[-1]] < curr:
                stack1.pop()
            while stack2 and nums[stack2[-1]] > curr:
                stack2.pop()
            nge[i] = (stack1[-1] - i) if stack1 else (n - i)
            nse[i] = (stack2[-1] - i) if stack2 else (n - i)
            stack1.append(i)
            stack2.append(i)

        stack1, stack2 = [], []
        for i in range(n):
            curr = nums[i]
            while stack1 and nums[stack1[-1]] <= curr:
                stack1.pop()
            while stack2 and nums[stack2[-1]] >= curr:
                stack2.pop()
            pge[i] = (i - stack1[-1]) if stack1 else (i + 1)
            pse[i] = (i - stack2[-1]) if stack2 else (i + 1)
            stack1.append(i)
            stack2.append(i)

        result = 0
        for i in range(n):
            max_contrib = nums[i] * pge[i] * nge[i]
            min_contrib = nums[i] * pse[i] * nse[i]
            result += max_contrib - min_contrib
        return result
