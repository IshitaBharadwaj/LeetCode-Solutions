class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        int profit[k + 1][n + 1];
        for (int i = 0; i <= k; i++) {
            profit[i][0] = 0;
        }
        for (int i = 0; i <= n; i++) {
            profit[0][i] = 0;
        }
        for (int i = 1; i <= k; i++) {
            for (int j = 1; j < n; j++) {
                int currMax = INT_MIN;
                for (int day = 0; day < j; day++) {
                    currMax = max(currMax, prices[j] - prices[day] + profit[i - 1][day]);
                }
                profit[i][j] = max(profit[i][j - 1], currMax);
            }
        }
        return profit[k][n - 1]; 
        
            
    }
};




/*
int maxProfit(int k, vector<int>& prices) {
        vector<int> vect2;
        vector<int> vect3;
        int sum=0;
        do{
            int n= prices.size();

            int maximum=*max_element(prices.begin(),prices.end());
            int pos_max = max_element(prices.begin(),prices.end()) - prices.begin();
            // copy(&prices[0],&prices[pos_max], back_inserter(vect2)); 
            // copy(&prices[pos_max+1],&prices[n], back_inserter(vect3)); 
            vect2.assign(&prices[0],&prices[pos_max]);
            vect3.assign(&prices[pos_max+1],&prices[n]);
            // vector<int> vect2(&prices[0],&prices[pos_max]);
            // vector<int> vect3(&prices[pos_max+1],&prices[n]);
            printf("\nvect2\n");
            for(auto i=vect2.begin();i!=vect2.end();i++)
            {
                printf("%d ",*i);
            }
            printf("\n vect2.size(): %d\n",vect2.size());
            // printf("\n");
            if(vect2.size()==0)
            {
                prices.assign(vect3.begin(), vect3.end()); 
                printf("\nprices\n");
                for(auto i=prices.begin();i!=prices.end();i++)
                {
                    printf("%d ",*i);
                }
                printf("\n");
                continue;
            }
            int minimum = *min_element(vect2.begin(),vect2.end());
            int pos_min = min_element(vect2.begin(),vect2.end()) - vect2.begin();
            printf("%d\n",maximum-minimum);
            printf("max= %d\n",maximum);
            printf("min= %d\n",minimum);            
            sum+=maximum-minimum;
            //prices=vect3;
            prices.assign(vect3.begin(), vect3.end()); 

            //copy(&vect3[0],&vect3[vect3.size()], back_inserter(prices)); 

            printf("\nprices\n");
            for(auto i=prices.begin();i!=prices.end();i++)
            {
                printf("%d ",*i);
            }
            k--;
        }while(vect3.size()>1 && k>0);
        // printf("vect3.size: %d",vect3.size());
        return sum;   
        
            
    }
*/