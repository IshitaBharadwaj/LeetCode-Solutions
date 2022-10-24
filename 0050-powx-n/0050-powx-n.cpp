class Solution {
public:
    double myPow(double x, int n) {
        if (n==0) return 1;
        if (n<0){
            n=abs(n);
            x=1/x;
        }
        return (n%2==0?myPow(x*x,n/2):x*myPow(x*x,n/2));
    }
};

// double myPow(double x, int n) {
//         if(n==0){
//             return 1;
//         }
//         if (n>0){
//             if (n==1){
//                 return x;
//             }

//             return myPow(x,n-1)*x; 
//         }
//         if (n<0){
//             if (n==-1)
//                 return (1/x);
//             return myPow(x,n+1)*(1/x);
//         }
//         return myPow(x,n);
//     }