class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        # a=[]
        # a=list(s)
        sum=0
        i=0
        
        m={}
        m['I']=1;
        m['V']=5;
        m['X']=10;
        m['L']=50;
        m['C']=100;
        m['D']=500;
        m['M']=1000;
        
        while i<n-1:
            if m[s[i]]<m[s[i+1]]:
                #print("s[i]: ",s[i]," s[i+1]: ",s[i+1])
                sum-=m[s[i]]
                sum+=m[s[i+1]]
                i+=2
            
            else:
                #print("s[i]: ",s[i])
                sum+=m[s[i]] 
                i+=1
        if i==n-1:
            sum+=m[s[i]]
        return sum