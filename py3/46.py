class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        curr = []

        def rec(i, n):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i % len(nums)])
            rec(i + 1, n + 1)
            curr.pop()
            curr.append(nums[(i + 1) % len(nums)])
            rec(i + 2, n + 1)

        for i in range(len(nums)):
            rec(i, 0)
        return res


sol = Solution()
print(sol.permute([1, 2, 3]))
