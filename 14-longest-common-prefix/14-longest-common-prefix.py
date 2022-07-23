class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n=len(strs)
        m=len(strs[0])
        for i in range(m):
            c=strs[0][i]
            for j in range(1,n):
                if i==len(strs[j]) or strs[j][i]!=c:
                    return strs[0][0:i:1]
        return strs[0]