# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if there are left and right; swap and call left and right
        def invert(node):
            node.left, node.right = node.right, node.left
            
            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)
        if root:
            invert(root)
        return root