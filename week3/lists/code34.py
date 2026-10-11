class Solution:
    def minOperation(self, n):
        """
        Input: integer n
        Output: minimum number of operations to reach n from 0
        """
        operations = 0

        while n > 0:
            if n % 2 == 0:
                n //= 2
            else:
                n -= 1
            operations += 1

        return operations
