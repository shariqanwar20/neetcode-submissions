# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # run dfs to get height
        self.balanced = True
        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # if height difference greater than 1 return false
            if abs(right - left) > 1:
                self.balanced = False
            
            return 1 + max(left, right)

        dfs(root)
        return self.balanced
        

        

        