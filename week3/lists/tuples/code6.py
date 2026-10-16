class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]
        
        for num in nums:
            new_subsets = []
            for s in subsets:
                new_subsets.append(s + [num])
            subsets += new_subsets
            
        return subsets
