class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        # if length!=3:
        #     return 0
        count=0
        max=0
        
        while count<=(length-3):
            l=nums[count]
            m=nums[count+1]
            n=nums[count+2]
            if l+m>n and m+n>l and l+n>m and abs(l-m)<n and abs(m-n)<l and abs(l-n)<m:
                sum=l+m+n
                if max<sum:
                    max=sum
            count+=1
        return max

            
            