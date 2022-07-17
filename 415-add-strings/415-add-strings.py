class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res1 = 0
        res2 = 0
  
   
        for i in range(len(num1)):
            res1 = res1 * 10 + (ord(num1[i]) - ord('0'))
            
        for i in range(len(num2)):
            res2 = res2 * 10 + (ord(num2[i]) - ord('0'))
  
        res3=res1+res2
        res3=str(res3)
        return res3
  