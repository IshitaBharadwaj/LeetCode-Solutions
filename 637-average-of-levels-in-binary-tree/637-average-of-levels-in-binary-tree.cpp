/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
    
        vector<double> ans;
        queue<TreeNode*> q;
        double sum=0;
        int n;
        
        q.push(root);
        TreeNode* p;
        
        while(!q.empty()){
            n=q.size();
            sum=0;
            for(int i=0;i<n;i++)
            {
                p=q.front();
                q.pop();
                if (p->left!=NULL){
                    q.push(p->left);
                }
                if (p->right!=NULL){
                    q.push(p->right);
                }
                sum+=p->val;
            }

            ans.push_back(sum/n);
            
            
        }
        return ans;
            
        
    }
};