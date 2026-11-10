class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        # dp[i] will store the minimum cost to reach step i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Starting at step 0 costs nothing
        
        # Calculate the minimum cost for each step up to n
        for i in range(1, n + 1):
            # Check previous steps that can reach i (i-1, i-2, i-3)
            for j in range(max(0, i - 3), i):
                jump_cost = costs[i - 1] + (i - j) ** 2
                dp[i] = min(dp[i], dp[j] + jump_cost)
                
        return dp[n]
