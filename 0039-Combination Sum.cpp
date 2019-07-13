class Solution {
public:
	vector<vector<int>>re;
	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		vector<int>comb;
		for (int i = 0; i < candidates.size(); i++)
			fun(candidates, target - candidates[i], i, comb);
		return re;
	}
	void fun(vector<int>candidates, int target, int index, vector<int>comb){
		comb.push_back(candidates[index]);
		if (target == 0){
			re.push_back(comb);
			comb.pop_back();
			return;
		}
		else if (target<0){
			comb.pop_back();
			return;
		}
		else{
			for (int i = index; i<candidates.size(); i++){
				fun(candidates, target - candidates[i], i, comb);
			}
		}
	}
};
