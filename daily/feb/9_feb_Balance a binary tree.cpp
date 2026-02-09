#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int x) {
        val = x;
        left = nullptr;
        right = nullptr;
    }
};

class Solution {
public:
    TreeNode* balanceBST(TreeNode* root) {
        vector<int> inorder;

        inorderTraversal(root, inorder);

        return buildBalancedBST(inorder, 0, inorder.size() - 1);
    }

private:
    void inorderTraversal(TreeNode* root, vector<int>& inorder) {
        if (!root) return;

        inorderTraversal(root->left, inorder);
        inorder.push_back(root->val);
        inorderTraversal(root->right, inorder);
    }

    TreeNode* buildBalancedBST(const vector<int>& inorder, int left, int right) {
        if (left > right) return nullptr;

        int mid = left + (right - left) / 2;

        TreeNode* root = new TreeNode(inorder[mid]);
        root->left = buildBalancedBST(inorder, left, mid - 1);
        root->right = buildBalancedBST(inorder, mid + 1, right);

        return root;
    }
};

void printInorder(TreeNode* root) {
    if (!root) return;

    printInorder(root->left);
    cout << root->val << " ";
    printInorder(root->right);
}

TreeNode* insertBST(TreeNode* root, int val) {
    if (!root) return new TreeNode(val);

    if (val < root->val)
        root->left = insertBST(root->left, val);
    else
        root->right = insertBST(root->right, val);

    return root;
}

int main() {
    TreeNode* root = nullptr;

    int arr[] = {10, 5, 1, 7, 40, 50};

    for (int x : arr) {
        root = insertBST(root, x);
    }

    cout << "Original BST (Inorder): ";
    printInorder(root);
    cout << endl;

    Solution s;
    root = s.balanceBST(root);

    cout << "Balanced BST (Inorder): ";
    printInorder(root);
    cout << endl;

    return 0;
}
