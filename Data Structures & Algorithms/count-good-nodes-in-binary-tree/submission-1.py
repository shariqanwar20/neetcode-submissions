# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs
        self.count = 0
        def dfs(node, path_max):
            # at each point node will have the maximum value in its path
            if not node:
                return None
            # if val <= node's val: good node
            if path_max <= node.val:
                self.count += 1
            
            if node.left:
                dfs(node.left, max(path_max, node.val))
            if node.right:
                dfs(node.right, max(path_max, node.val))
        
        dfs(root, -math.inf)
        return self.count

        