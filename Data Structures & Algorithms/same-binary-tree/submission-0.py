# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # dfs that runs simultaneously on both trees

        def dfs(np, nq):
            if not np and not nq:
                return True

            if np and not nq:
                return False

            if nq and not np:
                return False
            
            
            left = dfs(np.left, nq.left)
            right = dfs(np.right, nq.right)
            
            return (np.val == nq.val) and left and right
        
        return dfs(p, q)