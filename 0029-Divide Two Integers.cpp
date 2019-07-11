class Solution {
public:
    int divide(int dividend, int divisor) {
        long res = 0;
        bool positive = ((dividend < 0) == (divisor < 0));
        
        long dividend2 = labs(dividend);
        long divisor2 = labs(divisor);
        while(dividend2 >= divisor2){
            long temp = divisor2;
            long i = 1;
            // 指加速，不然溢出
            while(dividend2 >= temp){
                res += i;
                dividend2 -= temp;
                temp = temp << 1;
                i= i << 1;
            }
            
        }
        if(!positive){
            res = -res;
        }
        if(res < INT_MIN){
            res = INT_MIN;
        }
        if(res > INT_MAX){
            res = INT_MAX;
        }
        
        return res;
    }
};