# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
        DFS with explicit stack container
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        ans, stack = [], [(root, 0)]  # stack holds (node, level)
        
        while stack:
            node, level = stack.pop()
            # If this level has not been recorded yet
            if level == len(ans):
                ans.append(node.val)

            # Push left first so right is processed first
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return ans