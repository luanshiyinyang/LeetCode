class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        std::vector<int>::iterator index;
        while((index = std::find(nums.begin(), nums.end(), val)) != nums.end()){
            nums.erase(index);
        }
        return nums.size();
    }
};