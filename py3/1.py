class Solution:
    def twoSum_bruteforce(self, nums: list[int], target: int) -> list[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num1 + num2 == target:
                    return [i, j]
        return [-1, -1]

    def twoSum_map(self, nums: list[int], target: int) -> list[int]:
        index = {}
        # index the nums
        for i, num in enumerate(nums):
            index[num] = i

        print(index)
        # find
        for i, num in enumerate(nums):
            if target - num in index and i != index[target - num]:
                return [i, index[target - num]]

    def twoSum_map_onepass(self, nums: list[int], target: int) -> list[int]:
        index = {}
        for i, num in enumerate(nums):
            if target - num in index and i != index[target - num]:
                return [i, index[target - num]]
            else:
                index[num] = i


sol = Solution()
# print(sol.twoSum_map_onepass([2, 7, 11, 15], 9))
print(sol.twoSum_map_onepass([3, 3], 6))
