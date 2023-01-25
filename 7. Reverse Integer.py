class Solution:
    def reverse(self, x: int) -> int:
        string_x = str(x)
        if x < 0:
            reversed_x = int('-' + string_x[1:][::-1])
        else:
            reversed_x = int(string_x[::-1])

        if reversed_x < -2**31 or reversed_x > 2**31-1:
            return 0
        else:
            return reversed_x
