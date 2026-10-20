class Solution:
    def minimumStep(self, n: int) -> int:
        steps = 0
        while n > 1: n, steps = (n // 3 if n % 3 == 0 else n - 1), steps + 1
        return steps
