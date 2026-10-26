class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # Initialize the tracker variables with the first element
        min_so_far = arr[0]
        current_min = arr[0]
        
        # Iterate through the array starting from the second element
        for i in range(1, len(arr)):
            # Decide whether to add the current element to the existing subarray 
            # or start a new subarray from the current element
            current_min = min(arr[i], current_min + arr[i])
            
            # Update the global minimum sum found so far
            min_so_far = min(min_so_far, current_min)
            
        return min_so_far
