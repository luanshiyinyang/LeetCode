/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root){
            return dfs(root, 1);
        }
        else{
            return 0;
        }
    }
    
    int dfs(TreeNode* root, int depth){
        if(root->left && root ->right){
            return 1 + max(dfs(root->left, depth), dfs(root->right, depth));
        }
        if(root->left){
            return 1 + dfs(root->left, depth);
        }
        if(root->right){
            return 1 + dfs(root->right, depth);
        }
        return depth;
    }
};