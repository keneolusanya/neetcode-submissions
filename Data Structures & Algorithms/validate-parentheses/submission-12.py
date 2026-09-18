class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s) == 1:
        #     return False

        pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for b in s:
            if b in pairs:
                stack.append(b)

            else:
                if not stack or pairs[stack[-1]] != b:
                    return False
                else:
                    stack.pop()
        
        return (len(stack) == 0)
        
