class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=str(s)
        s=list(s)
        n=len(s)
        word=[]
        word1=[]
        for i in range(n):
            if s[i]!=' ':
                word.append(s[i])
                word1=word
            else:
                word=[]
        if not word:
            return len(word1)
        return len(word)