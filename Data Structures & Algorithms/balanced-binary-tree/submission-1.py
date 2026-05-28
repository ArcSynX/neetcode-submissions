# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # key: recusion 
        # we ask every node, the depth of its left child and right child 
        # brute force
        if not root:
            return True
        def max_depth(root): # recusion
            if not root: 
                return 0
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)

            return 1 + max(left_depth, right_depth)

        left_height = max_depth(root.left)
        right_height = max_depth(root.right)

        if abs(left_height - right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)


