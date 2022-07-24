class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        maxLen = []
        for rect in rectangles:
            maxLen.append(min(rect[0],rect[1]))
            
        maximum= max(maxLen)
        return maxLen.count(maximum)