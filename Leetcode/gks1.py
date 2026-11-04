class Solution:
    def subarrayXor(self, arr):
        n = len(arr)
        # If the length of the array is even, every element appears 
        # an even number of times across all subarrays, resulting in a total XOR of 0.
        if n % 2 == 0:
            return 0
        
        # If the length is odd, only elements at even indices (0, 2, 4, ...) 
        # appear an odd number of times.
        res = 0
        for i in range(0, n, 2):
            res ^= arr[i]
            
        return res
