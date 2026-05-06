class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        for char in tokens:
            if char in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[char](int(a),int(b)))
            else:
                stack.append(char)
        return int(stack[0])