class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapper = {}
        max_len = 0
        l = 0

        for r in range(len(s)):
            curr = s[r]

            while curr in mapper:
                left = s[l]
                mapper[left] -= 1
                l += 1
                if mapper[left] == 0:
                    del mapper[left]

            mapper[curr] = mapper.get(curr, 0) + 1
            max_len = max(max_len, r - l + 1)

        return max_len
            