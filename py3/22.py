class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = ["("]

        def gen(open, close):
            if open == close == n:
                res.append("".join(stack))
                return
            if open < n:
                stack.append("(")
                gen(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                gen(open, close + 1)
                stack.pop()

        gen(1, 0)
        return res


sol = Solution()
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(8))
