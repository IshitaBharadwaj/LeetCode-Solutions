class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        vector<vector<int>> dp(m , vector<int> (n , 0));
        dp[0][0]=grid[0][0];
        int up,left;
        
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++){
                if (i==0 and j==0){
                    continue;
                }
                up=i>=1?grid[i][j]+dp[i-1][j]:1e7;
                left=j>=1?grid[i][j]+dp[i][j-1]:1e7;
                
                dp[i][j]=min(up,left);
            }
        }
        return dp[m-1][n-1];
    }
};