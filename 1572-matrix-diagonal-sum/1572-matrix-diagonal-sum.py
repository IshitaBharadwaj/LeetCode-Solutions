class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m=len(mat)
        n=len(mat[0])
        print("n= ",n)
        print("m= ",m)
        sum=0
        for i in range(m):
            for j in range(n):
                if i==j  or i+j==n-1:
                    sum+=mat[i][j]
                    print("sum= ",sum)
        # if n%2==1 and m%2==1:
        #     i=(m-1)/2
        #     j=(n-1)/2
        #     sum-=mat[i][j]
        print(sum)
        return sum