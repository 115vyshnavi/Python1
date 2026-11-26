class Solution:

    def maximumSubarray(self, arr: list[int]) -> int:
        if not arr:
            return 0
            
        # Initialize dynamic programming states for the first element
        no_square = arr[0]
        one_square = arr[0] * arr[0]
        max_sum = one_square
        
        # Traverse through the remaining elements
        for i in range(1, len(arr)):
            x = arr[i]
            
            # Temporary state variables to avoid updating before evaluating both paths
            next_no_square = max(x, no_square + x)
            next_one_square = max(x * x + max(0, no_square), one_square + x)
            
            no_square = next_no_square
            one_square = next_one_square
            
            max_sum = max(max_sum, one_square)
            
        return max_sum
