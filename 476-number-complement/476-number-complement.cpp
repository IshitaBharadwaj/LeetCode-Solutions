class Solution {
public:
    int findComplement(int num) {
        int comp=0;
        int i=0;
        while(num>0){
            //printf("num: %d\n",num);
            if((num&1)==0){
                comp+=(1<<i);
            }
            i++;
            num=num>>1;

        }
        return comp;
    }
};