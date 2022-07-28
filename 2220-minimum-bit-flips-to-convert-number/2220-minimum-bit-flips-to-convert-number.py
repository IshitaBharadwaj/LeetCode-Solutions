class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        result=start ^ goal
        result=bin(result)
        result=str(result)
        # print("result: ",result)
        c = result.count("1")
        # print(c)
        return c