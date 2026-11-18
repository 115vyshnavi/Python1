class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        def backtrack(current, open_count, close_count):
            # Base case: valid combination of length 2*n is complete
            if len(current) == 2 * n:
                res.append("".join(current))
                return
            
            # Add an open parenthesis if we haven't reached the limit n
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()  # Backtrack
                
            # Add a close parenthesis if it matches an unclosed open parenthesis
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()  # Backtrack
                
        backtrack([], 0, 0)
        return res
