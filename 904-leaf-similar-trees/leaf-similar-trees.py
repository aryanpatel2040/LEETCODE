# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = [] # empty leaf1 array
        leaf2 = [] # empty leaf2 array

        def getLeaf(root, result): # recursive function with root and result as parameters
            if root.left is None and root.right is None: # basecase states that if root.left is none and root.right is also none
                result.append(root.val) # then we append the current root's val to result
                return

            if root.left: # if root.left exists
                getLeaf(root.left,result) # calling the function with root.left and result as parameter
            
            if root.right: # if root.right exists
                getLeaf(root.right, result) # calling the function and passing the parameter
            return # returning it after
        getLeaf(root1, leaf1) # function call
        getLeaf(root2, leaf2) # function call
        return leaf1 == leaf2 # returning true if they are equal