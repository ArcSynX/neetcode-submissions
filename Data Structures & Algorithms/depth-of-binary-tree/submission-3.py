# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # maxdepth(root) = 1 + max(depth of left subtree, depth of right subtree)
        # recursion
        if not root:
            return 0
        leftdepth = self.maxDepth(root.left)
        rightdepth = self.maxDepth(root.right)

        return 1 + max(leftdepth, rightdepth)
        
        