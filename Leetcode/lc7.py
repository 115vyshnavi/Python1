class Solution(object):
    def reverse(self, x):
        s = str(abs(x))
        reversed_s = s[::-1]
        result = int(reversed_s)
        if x < 0:
            result = -result
        if result < -(2**31) or result > 2**31 - 1:
            return 0
        return result