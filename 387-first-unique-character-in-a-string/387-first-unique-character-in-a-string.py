class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        for i in range(len(s)):
            j=i
            if (s[j] not in s[i+1:n]) and (s[j] not in s[0:i]):
                return j
            
        return -1