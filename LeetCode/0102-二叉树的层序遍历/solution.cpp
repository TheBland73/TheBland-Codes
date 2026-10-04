#include <vector>
#include <queue>

using namespace::std;


//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    // 构造函数
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root){
            return {};
        }
        vector<vector<int>> res;   
        queue<TreeNode*> q;

        q.push(root);

        while(!q.empty()){
            int size = q.size();
            vector<int> level;
            level.reserve(size); //预分配，防止额外开辟内存，拖慢速度

            for(int i=0;i<size;++i){
                TreeNode* node = q.front();
                q.pop();

                level.push_back(node->val);

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
            res.push_back(level);
        }
        return res;
    }
};

 
// class Solution {
// public:
//     vector<vector<int>> levelOrder(TreeNode* root) {
//         vector<vector<int>> res;
//         if (root == nullptr){
//             return res;
//         }

//         queue<TreeNode*> q;
//         q.push(root);
//         res.push_back({root->val});

//         while (!q.empty()){
//             int size = q.size();
//             vector<int> ans;
//             for(int i = 0;i < size; ++i){
//                 TreeNode* node = q.front();
//                 q.pop();
//                 if (node->left != nullptr){
//                     q.push(node->left);
//                     ans.push_back(node->left->val);
//                 }
//                 if (node->right != nullptr){
//                     q.push(node->right);
//                     ans.push_back(node->right->val);
//                 }
//             }
//             if(!ans.empty()){
//                 res.push_back(ans);
//             }
//         }
//         return res;
//     }
// };
