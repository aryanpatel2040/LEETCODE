class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left,val)
        elif val > root.val:
            return self.searchBST(root.right,val) 