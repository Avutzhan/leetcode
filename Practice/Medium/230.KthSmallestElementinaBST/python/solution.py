# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []
        def doInOrderDFS(node):
            if not node:
                return
            doInOrderDFS(node.left)
            inOrder.append(node.val)
            doInOrderDFS(node.right)

        doInOrderDFS(root)
        return inOrder[k-1]