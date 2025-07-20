class Solution(object):
    def topKFrequent(self, nums, k):
        countFreq = defaultdict(int)

        for val in nums:
            countFreq[val] += 1

        values = [[] for _ in range(len(nums) + 1)]
        for key, val in countFreq.items():
            values[val].append(key)

        res = []

        for val in list(reversed(values)):
            for v in val:
                res.append(v)
                if len(res) == k:
                    return res
