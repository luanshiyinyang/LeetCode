class Solution {
public:
    string simplifyPath(string path) {
        string temp, res;
        vector<string> stk;
        stringstream ss(path);
        while(getline(ss, temp, '/')){
            if(temp == "" || temp == ".") continue;
            if(temp == ".." && !stk.empty()) stk.pop_back();
           
            else if (temp != "..") stk.push_back(temp); 
        }
        for(int i=0;i<stk.size();i++){
            res += "/" + stk[i];
        }
        return res.empty() ? "/":res;
        
    }
};