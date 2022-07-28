class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        n=len(nums)
        sum=0
        opt=[]
        for i in range(n):
            sum=sum*2+nums[i]
            # print("sum: ",sum)
            if sum%5 == 0:
                opt.append(True)  
            else:
                opt.append(False)
        # print(opt)
        return opt