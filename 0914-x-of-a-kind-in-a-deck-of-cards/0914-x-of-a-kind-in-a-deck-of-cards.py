class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        unique = list(set(deck));
        clist=[]
        globalcounter = deck.count(unique[0])
        for i in unique:
            counter = deck.count(i)
            if counter<2:
                return False
            clist.append(counter)
        
        x=2
        flag=0
        m=min(clist)
        while x<=m:
            for i in range(len(clist)):
                if clist[i]%x==0:
                    flag=1
                else:
                    flag=0
                    break
            if flag==1:
                return True
            x+=1
        return False

# def hasGroupsSizeX(self, deck):
#         """
#         :type deck: List[int]
#         :rtype: bool
#         """
#         unique = list(set(deck));
#         globalcounter = deck.count(unique[0])
#         for i in unique:
#             counter = deck.count(i)
#             if counter !=globalcounter or counter==1:
#                 return False
#         return True