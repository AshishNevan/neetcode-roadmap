import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        n = len(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            curr = 0
            for p in piles:
                curr += math.ceil(p / mid)
            if curr > h:
                l = mid + 1
            if curr <= h:
                r = mid - 1
                res = mid
        return res


sol = Solution()
print(sol.minEatingSpeed([3, 6, 7, 11], 8))
