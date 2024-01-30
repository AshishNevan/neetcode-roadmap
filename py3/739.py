class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0]
        max_idx = 0
        maxima= 0
        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] > temperatures[i + 1]:
                x = res.pop()
                res.push(x)
                res.push(x)
            else:
                

        return res[::-1]


sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 100, 72, 98]))
