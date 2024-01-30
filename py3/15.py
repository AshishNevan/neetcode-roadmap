from collections import Counter


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                print("skipped i", i)
                continue
            l, r = i + 1, len(nums) - 1
            print("i,l,r", (i, l, r))
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    print("found at ", (i, l, r))
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    print("i,l,r", (i, l, r))
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    print("i,l,r", (i, l, r))
                else:
                    r -= 1
                    print("i,l,r", (i, l, r))
        return res


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([0, 1, 1]))
print(sol.threeSum([1, -1, -1, 0]))
print(sol.threeSum([0, 0, 0, 0]))
print(sol.threeSum([3, 0, -2, -1, 1, 2]))
