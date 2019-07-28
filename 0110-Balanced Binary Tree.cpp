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
    bool isBalanced(TreeNode* root) {
        if(!root){
            return true;
        }
        return abs(get_height(root->left) - get_height(root->right)) < 2 && isBalanced(root->left) && isBalanced(root->right); 
            
    }
    int get_height(TreeNode* root){
        if(!root){
            return 0;
        }
        return 1 + max(get_height(root->left), get_height(root->right));
    }
};