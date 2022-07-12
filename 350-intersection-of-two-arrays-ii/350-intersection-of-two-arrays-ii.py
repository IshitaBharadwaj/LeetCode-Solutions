class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        final=[]
        n=len(nums1)
        m=len(nums2)
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        #k=0
        while i<n and j<m:
            if nums1[i]==nums2[j]:
                final.append(nums1[i])
                # k+=1
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        print(final)
        return(final)