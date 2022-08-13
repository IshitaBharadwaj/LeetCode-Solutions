class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        int len = bits.size();
        int pos = 0;
        bool one = true;
        for (int i = 0; i < len; i++) {
            one = true;
            if (bits[i] == 1) {
                i++;
                one = false;
            }
        }
        return one; 
    }
};