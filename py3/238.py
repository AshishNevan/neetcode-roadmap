class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre = [[] for _ in range(len(nums))]
        post = [[] for _ in range(len(nums))]
        pre[0] = 1
        post[-1] = 1
        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]
            post[-i - 1] = post[-i] * nums[-i]
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
        return res


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
