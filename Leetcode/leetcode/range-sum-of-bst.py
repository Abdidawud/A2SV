# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=0
        def inorder(node,low,high):
            nonlocal ans
            if not node:
                return []
            inorder(node.left,low,high)
            if node.val>=low and node.val<=high:
                ans+=node.val
            inorder(node.right,low,high)
        inorder(root,low,high)
        return ans