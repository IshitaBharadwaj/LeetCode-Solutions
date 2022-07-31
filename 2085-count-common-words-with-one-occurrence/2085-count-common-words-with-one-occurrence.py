class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        m=len(words1)
        n=len(words2)
        c=0
        if n>m:
            for i in words1:
                if i in words2:
                    num1=words1.count(i)
                    num2=words2.count(i)
                    if num1==1 and num2==1:
                        c+=1
        else:
            for i in words2:
                if i in words1:
                    num1=words1.count(i)
                    num2=words2.count(i)
                    if num1==1 and num2==1:
                        c+=1
        print(c)
        return c
                    