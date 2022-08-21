class Solution {
public:
    int specialArray(vector<int>& nums) {
        int max = *max_element(nums.begin(), nums.end());    
        int n=nums.size();
        int count=0;
        for(int i=0;i<=max;i++){
            count=0;
            for(int j=0;j<n;j++){
                if (i<=nums[j]){
                    count++;
                }
            }
            if(i==count){
                return i;
            }
        }
        return -1;
    }
};