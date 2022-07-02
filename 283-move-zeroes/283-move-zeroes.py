class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        j=0
        for i in range(n):
            if nums[i]!=0:
                temp = nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j+=1
        print(nums)
        return nums