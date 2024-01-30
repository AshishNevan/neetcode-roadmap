class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        curr = []
        candidates.sort()

        def backtrack(i, t):
            if t == 0:
                res.append(curr.copy())
                return
            if i == len(candidates) or t < candidates[i]:
                return
            curr.append(candidates[i])
            backtrack(i, t - candidates[i])
            curr.pop()
            backtrack(i + 1, t)

        backtrack(0, target)
        return res


sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
