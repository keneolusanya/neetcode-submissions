class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for l in s:
            if(l == ')'):
                if len(my_stack) == 0 or my_stack[-1] != '(':
                    return False
                else:
                    my_stack.pop()

            elif(l == '}'):
                if len(my_stack) == 0 or my_stack[-1] != '{':
                    return False
                else:
                    my_stack.pop()

            elif(l == ']'):

                if len(my_stack) == 0 or my_stack[-1] != '[':
                    return False
                else:
                    my_stack.pop()

            else:        
                my_stack.append(l)

            print(my_stack)
        

        return len(my_stack) == 0