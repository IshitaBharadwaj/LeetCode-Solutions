class Solution(object):
    # def sumOfEvens(self,arr):
    #     sum=0
    #     for i in range(len(arr)):
    #         if arr[i]%2==0:
    #             sum+=arr[i]
    #     return sum
    
    def sumEvenAfterQueries(self, A, queries):
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ans.append(S)

        return ans
    
    # My soln
    # def sumEvenAfterQueries(self, nums, queries):
    #     """
    #     :type nums: List[int]
    #     :type queries: List[List[int]]
    #     :rtype: List[int]
    #     """
    #     n=len(queries)
    #     answer=[]
    #     for i in queries:
    #         val=i[0]
    #         index=i[1]
    #         nums[index]+=val
    #         # evensum=self.sumOfEvens(nums)
    #         evensum=sum(x for x in nums if x % 2 == 0)
    #         answer.append(evensum)
    #     return answer