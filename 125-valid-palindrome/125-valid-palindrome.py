class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        l=[ch for ch in s if ch.isalnum()]
        s1=''.join(l)
        s2=s1[::-1]
        if s1==s2:
            return True
        return False