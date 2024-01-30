class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snowball = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                snowball += 1
                i += 1
            else:
                nums[i], nums[i - snowball] = nums[i - snowball], nums[i]
                i += 1
        print(nums)


sol = Solution()
sol.moveZeroes([0, 1, 0, 3, 12])
