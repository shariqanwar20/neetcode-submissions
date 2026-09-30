# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        self.ind = 0
        def construct(inorder):
            if self.ind not in range(len(preorder)) or not inorder:
                return None
            
            # find root in in-order
            mid = inorder.index(preorder[self.ind])
            node = TreeNode(preorder[self.ind])

            self.ind += 1
            # construct left sub-tree; [:root_index]
            node.left = construct(inorder[:mid])
            
            # construct right sub-tree; [root_index+1:]
            node.right = construct(inorder[mid+1:])

            return node

        root = construct(inorder)
        
        return root