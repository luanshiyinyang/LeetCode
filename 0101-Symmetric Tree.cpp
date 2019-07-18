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
    bool isSymmetric(TreeNode* root) {
        return root == nullptr || bfs(root->left, root->right);  // 截断判断
    }
    bool bfs(TreeNode* left, TreeNode* right){
        if(left == nullptr || right == nullptr){
            return left == right;
        }
        if(left->val != right->val){
            return false;
        }
        return bfs(left->left, right->right) && bfs(left->right, right->left);
    }
};