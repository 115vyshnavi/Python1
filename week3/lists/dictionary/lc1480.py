class Solution(object):
    def runningSum(self, nums):
        answer=[]
        total =0
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for current_number in nums:
            total = total + current_number
            answer.append(total)

        return answer
        
        