class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        i=0
        j=1
        while i<n and j<n:
            while i<n and nums[i]%2==0:
                i+=2
            while j<n and nums[j]%2==1:
                j+=2
            if i<n and j<n:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
        return nums