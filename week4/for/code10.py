class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        i = 0
        for num in range(3):
            for j in range(counts[num]):
                nums[i] = num
                i += 1