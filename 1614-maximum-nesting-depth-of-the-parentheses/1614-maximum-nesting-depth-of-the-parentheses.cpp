class Solution {
public:
    int maxDepth(string s) {
        stack<char> stack;
        int i=0,max=0,len;
        int n=s.length();
        for(i=0;i<n;i++){
            if(s[i]=='('){
                stack.push(s[i]);
            }
            if(s[i]==')'){
                len=stack.size();
                if(max<len){
                    max=len;
                }
                stack.pop();
            }
        }
        return max;
    }
};