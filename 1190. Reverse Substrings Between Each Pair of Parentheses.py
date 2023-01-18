class Solution:
    def reverseParentheses(self, s: str) -> str:
        char = list(s)
        bracket_index = []
        for i, j in enumerate(char):
            if j == '(':
                bracket_index.append(i)
            elif j == ')':
                a = bracket_index.pop()
                char[a:i] = char[i:a:-1]

        return "".join(j for j in char if j not in '()')
