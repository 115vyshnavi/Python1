class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # **The core idea is to count the total servers in each row and column first,**
        # **then check which servers share a row or column with at least one other server.**
        m = len(grid)
        n = len(grid[0])
        
        row_counts = [0] * m
        col_counts = [0] * n
        
        # First pass: pre-calculate how many servers exist in each row and column
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    row_counts[r] += 1
                    col_counts[c] += 1
                    
        communicating_servers = 0
        
        # Second pass: count a server if its row or column total is greater than 1
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    if row_counts[r] > 1 or col_counts[c] > 1:
                        communicating_servers += 1
                        
        return communicating_servers
