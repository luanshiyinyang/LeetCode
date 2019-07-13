#include "iostream"
#include "vector"
using namespace std;
class Solution {
public:
    vector<string> res;
    vector<string> generateParenthesis(int n) {
        this->solve("", n, n);
        return res;

    }
    void solve(string s, int left, int right){
        if(left==0&&right==0){
            res.push_back(s);
        }
        if(left>0){
            solve(s+"(", left-1, right);
        }
        if(left<right){
            solve(s+")", left, right-1);
        }
    }
};


int main(void){
    vector<string> s;
    s = Solution().generateParenthesis(3);
    for(int i=0; i<s.size();i++){
        cout<<s[i]<<endl;
    }

}
