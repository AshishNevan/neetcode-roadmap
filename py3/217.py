class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        hs = set()
        for i in nums:
            if i in hs:
                return True
            hs.add(i)
        return False


sol = Solution()
print(sol, sol.containsDuplicate([1, 2, 3, 1]))
print(sol, sol.containsDuplicate([1, 2, 3, 4]))
print(sol, sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
