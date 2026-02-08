class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (d:=lambda r:(inf,max(l:=d(r.left),r:=d(r.right))+1)[-2<l-r<2] if r else 0)(root)!=inf