class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.max_ans = 0


        def dfs_sum(node):
            if not node:
                return 0

            left_sum = dfs_sum(node.left)
            right_sum = dfs_sum(node.right)

            node.val = node.val + left_sum + right_sum
            return node.val

        total_sum = dfs_sum(root)

   
        def dfs_product(node):
            if not node:
                return

            product = node.val * (total_sum - node.val)
            self.max_ans = max(self.max_ans, product)

            dfs_product(node.left)
            dfs_product(node.right)

        dfs_product(root)

        return self.max_ans % MOD
