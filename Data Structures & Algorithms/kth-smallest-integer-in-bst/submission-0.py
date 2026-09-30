# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # run dfs
        self.curr = 0

        self.res = None

        def dfs(node):            
            if node.left:
                dfs(node.left)
            
            self.curr += 1
            # set value when its k
            if self.curr == k:
                self.res = node.val
                return None

            if node.right:
                dfs(node.right)

        dfs(root)
        return self.res
        

        # return that set value