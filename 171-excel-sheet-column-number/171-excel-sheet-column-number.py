class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        n=len(columnTitle)
        sum=0
        for i in range(n):
            asci = ord(columnTitle[i])
            num=asci-64
            sum=sum*26+num
        print(sum)
        return sum