import collections


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        hs = set(nums)
        longest = 0
        for num in hs:
            if (num - 1) not in hs:
                x = num
                length = 1
                while x + 1 in hs:
                    length += 1
                    x += 1
                longest = max(longest, length)
        return longest


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2, -3, -4, -5, -6, -7]))
