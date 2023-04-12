/*
 * @lc app=leetcode id=429 lang=cpp
 *
 * [429] N-ary Tree Level Order Traversal
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

    vector<vector<int>> out;
    void levelOrd(Node* current, int lvl){
        if (current == NULL) return;
        if (out.size() == lvl) out.push_back(vector<int>());
        out[lvl].push_back(current->val);
        for (auto child : current->children){
            levelOrd(child, lvl+1);
        }
    }

    vector<vector<int>> levelOrder(Node* root) {
        levelOrd(root, 0);
        return out;
    }
};
// @lc code=end

