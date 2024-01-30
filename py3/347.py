from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        f_map = Counter(nums)
        sorted_f_map = sorted(f_map, key=f_map.get, reverse=True)
        return sorted_f_map[:k]
        


sol = Solution()
print(sol.topKFrequent([3,2,2,1,1,1], 2))
print(sol.topKFrequent([1,2], 2))