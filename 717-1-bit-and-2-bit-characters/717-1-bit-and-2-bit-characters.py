class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n= len(bits)
        i=0
        zero=True
        while i<n:
            zero=True
            if bits[i]==1:
                zero =False
                i+=1
            i+=1
        return zero
             