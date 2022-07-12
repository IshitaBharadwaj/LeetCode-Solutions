class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count1=[]
        arr.sort()
        n=len(arr)
        i=0
        c=0
        while(i<n):
            j=i
            while(j<n):
                # print("arr[i]==arr[j]: ",arr[i],arr[j])
                if arr[i]==arr[j]:
                    c+=1
                    j+=1
                    if(j==n):
                        count1.append(c)
                else:
                    # print("count for i: ",i," and j: ",j," is c: ",c)
                    count1.append(c)
                    c=0
                    break
            i=j
        # print(count1)
        for elem in count1:
            if count1.count(elem) > 1:
                return False
        return True