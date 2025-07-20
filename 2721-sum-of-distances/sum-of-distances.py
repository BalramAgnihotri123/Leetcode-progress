class Solution(object):
    def distance(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        total = defaultdict(int)
        count = defaultdict(int)
        res = [0] * n

        for i in range(n):
            val = nums[i]
            res[i] += (i * count[val]) - total[val]

            total[val] += i
            count[val] += 1

        total = defaultdict(int)
        count = defaultdict(int)

        for i, val in reversed(list(enumerate(nums))):
            res[i] += total[val] - (i * count[val])

            total[val] += i
            count[val] += 1
            
        return res
