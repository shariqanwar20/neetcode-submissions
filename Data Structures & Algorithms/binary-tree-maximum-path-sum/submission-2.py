# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # we will keep a global res that keeps track of max path sum
        self.res = -math.inf

        # dfs
        # we will pass around path sum
        def dfs(node):
            if not node: return 0

            # find sum from left path
            left, right = 0, 0
            if node.left:
                left = dfs(node.left)

            # find sum from right path
            if node.right:
                right = dfs(node.right)

            left = max(left, 0)
            right = max(right, 0)

            # compare with res
            self.res = max(self.res, node.val + left + right)

            return node.val + max(left, right)
            
        dfs(root)
        return self.res
        