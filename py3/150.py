class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        op_stack = []
        for i in tokens:
            if i == "+":
                b = op_stack.pop()
                a = op_stack.pop()
                op_stack.append(int(a) + int(b))
            elif i == "-":
                b = op_stack.pop()
                a = op_stack.pop()
                op_stack.append(int(a) - int(b))
            elif i == "*":
                b = op_stack.pop()
                a = op_stack.pop()
                op_stack.append(int(a) * int(b))
            elif i == "/":
                b = op_stack.pop()
                a = op_stack.pop()
                op_stack.append(int(a) / int(b))
            else:
                op_stack.append(i)
        return op_stack[0]


sol = Solution()
print(sol.evalRPN(["2", "1", "+", "3", "*"]))
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
print(
    sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
)
