class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapper = {}

        for idx, num in enumerate(nums):
            if num in mapper and idx - mapper[num] <= k:
                return True

            mapper[num] = idx

        return False