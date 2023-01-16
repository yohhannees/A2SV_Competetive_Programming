class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            a = tokens[i]
            if a not in op:
                stack.append(a)
            elif a in op:
                b = int(stack.pop())
                c = int(stack.pop())
                if a == '+':
                    d = b + c
                    stack.append(d)
                elif a == '-':
                    d = c - b
                    stack.append(d)
                elif a == '*':
                    d = b * c
                    stack.append(d)
                elif a == '/':
                    d = int(c / b)
                    stack.append(d)
        return int(stack[0])
