class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        i = 0

        while i < len(nums) and nums[i] <= 0:
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return res


sol = Solution()
print(sol.threeSum([0, 0, 0, 0]))
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 0, 0]))
print(sol.threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
