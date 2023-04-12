/*
 * @lc app=leetcode id=589 lang=cpp
 *
 * [589] N-ary Tree Preorder Traversal
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

class Solution
{
public:
    vector<int> out;

    void preRecursive(Node *current)
    {
        if (current == nullptr)
            return;
        out.push_back(current->val);
        for (std::vector<Node *>::iterator it = current->children.begin(); it != current->children.end(); ++it)
        {
            preRecursive(*it);
        }
    }

    vector<int> preorder(Node *root)
    {
        preRecursive(root);
        return out;
    }
};
// @lc code=end

