/*
 * @lc app=leetcode id=590 lang=cpp
 *
 * [590] N-ary Tree Postorder Traversal
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> out;

    void postRecursive(Node *current)
    {
        if (current == nullptr)
            return;
        for (std::vector<Node *>::iterator it = current->children.begin(); it != current->children.end(); ++it)
        {
            postRecursive(*it);
        }
        out.push_back(current->val);
    }

    vector<int> postorder(Node *root)
    {
        postRecursive(root);
        return out;
    }
};
// @lc code=end

