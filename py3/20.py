class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "[{(":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == "}" and stack[len(stack) - 1] == "{":
                    stack.pop()
                    continue
                if c == "]" and stack[len(stack) - 1] == "[":
                    stack.pop()
                    continue
                if c == "]" and stack[len(stack) - 1] == "[":
                    stack.pop()
                    continue
                if c == ")" and stack[len(stack) - 1] == "(":
                    stack.pop()
                    continue
                return False

        return len(stack) == 0


sol = Solution()
print(sol.isValid("(){}()"))
