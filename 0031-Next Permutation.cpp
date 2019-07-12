class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int partition = -1;
        int n = nums.size();
        for(int i=n-2;i>-1;i--){
            if(nums[i]<nums[i+1]){
                partition = i;
                break;
            }
        }
        if(partition == -1){
            reverse(nums.begin(), nums.end());
        }
        else{
            for(int i=n-1;i>partition;i--){
                if(nums[i]>nums[partition]){
                    int temp = nums[i];
                    nums[i] = nums[partition];
                    nums[partition] = temp;
                    break;
                }
            }
            reverse(nums.begin()+partition+1, nums.end());
            
        }
    }
};