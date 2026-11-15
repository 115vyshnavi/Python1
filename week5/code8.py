class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s) - 1
        length = 0
        
        # 1. Skip any trailing spaces at the end of the string
        while i >= 0 and s[i] == ' ':
            i -= 1
            
        # 2. Count the characters of the last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
            
        return length
