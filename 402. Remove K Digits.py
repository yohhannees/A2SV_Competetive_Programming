class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        i, N = 0, len(num)
        stack = []
        if k >= len(num):
            return "0"
        while i < N:
            while stack and k > 0 and int(stack[-1]) > int(num[i]):
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while k > 0:
            stack.pop()
            k -= 1
        return str(int("".join(stack)))

        # Solution 2
        stack = []
        if k >= len(num):
            return "0"
        for c in num:
            while stack and k > 0 and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)
        stack = stack[:len(stack) - k]
        res = "".join(stack)
        return str(int(res))