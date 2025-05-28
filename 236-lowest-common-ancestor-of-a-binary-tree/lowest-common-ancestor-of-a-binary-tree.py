class Solution:
    def lowestCommonAncestor(self, root, p, q):


        def f(root, p, q):

            if not root:
                return None
            if root.val == p.val:
                return root
            if root.val == q.val:
                return root

            
            left = f(root.left, p, q)
            right = f(root.right, p, q)

            if left and right:
                return root

            return left if left else right


        return f(root, p, q)
        