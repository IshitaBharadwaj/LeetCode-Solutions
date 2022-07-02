class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        j=0
        for i in range(n):
            if nums[i]!=val:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j+=1
        # print(nums)
        k=0
        if len(nums)!=0:
            while k<n and nums[k]!=val:
                k+=1
        # print(k)
        return k