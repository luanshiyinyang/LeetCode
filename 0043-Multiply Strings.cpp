class Solution {
public:
    string multiply(string num1, string num2) {
        vector<int> rst(num1.size()+num2.size(), 0);
        int pos = rst.size() - 1;
        for(int i = num1.size()-1;i>=0;i--){
            int in_pos = pos;
            for(int j = num2.size()-1;j>=0;j--){
                rst[in_pos] += (int)(num1[i] - '0') * (int)(num2[j] - '0');
                rst[in_pos-1] += (int)(rst[in_pos] / 10);
                rst[in_pos] = rst[in_pos] % 10;
                in_pos -=1;
            }
            pos -= 1;
        }
        int place = 0;
        string res = "";
        while(place < rst.size() && rst[place] == 0){
            place += 1;
        }
        
        if(place == rst.size()){
            res = "0";
        }
        else{
            for(int i = place;i<rst.size();i++){
                res += (char)(rst[i] + '0');
            }
        }
        return res;
    }
};