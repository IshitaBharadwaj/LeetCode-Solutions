class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        vector<int> uni(deck);
        vector<int>::iterator it;
        sort(uni.begin(),uni.end());
        it = unique(uni.begin(),uni.end()) ;   
        uni.resize(distance(uni.begin(),it));
        vector<int> clist;
        
        printf("uni\n");
        for(int j=0;j<uni.size();j++){
            printf("%d ",uni[j]);
        }  
        printf("\n");
        int counter=0,i=0;
        int globalcounter = std::count(deck.begin(),deck.end(),uni[0]);
        // printf("globalcounter: %d",globalcounter);
        for(i=0;i<uni.size();i++){
            counter = std::count(deck.begin(),deck.end(),uni[i]);
            printf("counter: %d",counter);
            if (counter<2)
                return false;
            clist.push_back(counter);
        
        }
        printf("clist");
        for(int j=0;j<clist.size();j++){
            printf("%d ",clist[j]);
        }  
        printf("\n");
        int x=2;
        
        int flag=0;
        int m=*min_element(clist.begin(),clist.end());
        while (x<=m){
            for(i=0;i<clist.size();i++){
                if (clist[i]%x==0) flag=1;
                else{
                    flag=0;
                    break; 
                }
                    
            }
            if (flag==1)
                return true;
            x+=1;
        }
        return false;
        
    }
};