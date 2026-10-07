from typing import List
class Solution:
     def getDistinctDifference(self, arr): 
        a = []
        for i in range(1, len(arr) + 1):
            # Left side unique elements count
            l = len(set(arr[:i-1]))
            # Right side unique elements count
            r = len(set(arr[i:]))
            a.append(l - r)
            
        return a