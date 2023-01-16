class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        hashmap = {'}': '{', ']': '[', ')': '('}
        stack = []
        for char in s:
            if char in hashmap.values():
                stack.append(char)
            elif stack and hashmap[char] == stack[-1]:
                stack.pop()
            else:
                return (False)

        return len(stack) == 0
