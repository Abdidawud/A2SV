# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)


        def inserter(node,number):
            if node is None:
                return TreeNode(number)
            if number<node.val:
                node.left=inserter(node.left,number)
                return node
            if number>node.val:
                node.right=inserter(node.right,number)
                return node
        inserter(root,val)
        return root