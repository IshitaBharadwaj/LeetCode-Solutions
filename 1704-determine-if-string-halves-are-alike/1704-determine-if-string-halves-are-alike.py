class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n=len(s)
        s=s.lower()
        vowel1=0
        vowel2=0
        a=str()
        b=str()
        for i in range(n/2):
            a+=s[i]
            if s[i]=='a' or s[i]=='o' or s[i]=='e' or s[i]=='i' or s[i]=='u':
                vowel1+=1
        for j in range(n/2,n):
            b+=s[j]
            if s[j]=='a' or s[j]=='o' or s[j]=='e' or s[j]=='i' or s[j]=='u':
                vowel2+=1
        # print("a: ",a)
        # print("b: ",b)
        # print("vowel1: ",vowel1)
        # print("vowel2: ",vowel2)
        if vowel1==vowel2:
            return True
        return False
        