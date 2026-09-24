import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif t == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif t == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 * num1)
            elif t == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if num2 / num1 < 0:
                    stack.append(math.ceil(num2 / num1))
                else:
                    stack.append(num2 // num1)
            else:
                stack.append(int(t))
        
        return stack[0]


