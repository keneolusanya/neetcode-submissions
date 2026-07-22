class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # start with the empty stack
        # if you hit a number, you add to the stack
        # if you hit an operand, you perform that operand on the stack by
        # popping twice, then append the result back to the stack
        # once done with tokens array, pop from the stack as final result

        stack = []
        for t in tokens:
            if t == "+":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = num1 + num2
                stack.append(res)
            elif t == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 - num2
                stack.append(res)
            elif t == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                res = num1 * num2
                stack.append(res)
            elif t == "/":
                num2 = float(stack.pop())
                num1 = float(stack.pop())
                res = num1 / num2
                stack.append(int(res))
            else:
                stack.append(int(t))
            
        return stack.pop()
