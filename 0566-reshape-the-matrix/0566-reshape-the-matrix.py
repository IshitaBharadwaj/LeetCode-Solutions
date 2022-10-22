class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        # k=0
        # l=0
        if(m*n==r*c):
            opt=[]
            ele=[]
            for i in range(m):
                for j in range(n):
                    k=(i*n+j) %c
                    if k!=c-1:
                        ele.append(mat[i][j])
                    else:
                        ele.append(mat[i][j])
                        opt.append(ele)
                        ele=[]
            print(opt)
            return opt

        return mat
        