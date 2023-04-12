/*
 * @lc app=leetcode id=145 lang=cpp
 *
 * [145] Binary Tree Postorder Traversal
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

/*
Accepted
68/68 cases passed (6 ms)
Your runtime beats 20.6 % of cpp submissions
Your memory usage beats 90.63 % of cpp submissions (8.4 MB)
*/
class Solution
{
public:
    vector<int> out;

    void postRecursive(TreeNode *current)
    {
        if (current == nullptr)
            return;
        postRecursive(current->left);
        postRecursive(current->right);
        out.push_back(current->val);
    }
    vector<int> postorderTraversal(TreeNode *root)
    {
        postRecursive(root);
        return out;
    }
};
// @lc code=end
