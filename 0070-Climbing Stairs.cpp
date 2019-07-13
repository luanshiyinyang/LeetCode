#include "vector"
#include "iostream"
using namespace std;
class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(n+1, 0);
        for(int i = 0; i < n + 1; i++){
            if(i == 0 || i == 1){
                    dp[i] = 1;
            }
            else{
                dp[i] = dp[i-1] + dp[i-2];
            }
        }
        return dp[n];

    }
};

int main(void){
    cout<<Solution().climbStairs(10)<<endl;
    return 0;
}

