# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res

        to_do = deque()
        to_do.append(root)
        while to_do:
            level_nodes_size = len(to_do)
            level = []
            for i in range(level_nodes_size):
                # process all level nodes; append it to res
                node = to_do.popleft()
                level.append(node.val)

                # continually add new level nodes to queue
                if node.left:
                    to_do.append(node.left)
                if node.right:
                    to_do.append(node.right)
            res.append(level)
        return res
            