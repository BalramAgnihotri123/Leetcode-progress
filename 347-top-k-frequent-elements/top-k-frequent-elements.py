class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countFreq = {}
        for num in nums:
            countFreq[num] = countFreq.get(num, 0) + 1

        kElemFreq = [[] for _ in range(len(nums) + 1)]
        for key, val in countFreq.items():
            kElemFreq[val].append(key)
        
        kElemFreq = [item for sublist in kElemFreq for item in sublist]

        return kElemFreq[-k:]