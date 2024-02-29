# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node,max_val,min_val):
            if not node:
                return 0
            max_diff=max(abs(node.val-max_val),abs(node.val-min_val))

            max_val=max(max_val,node.val)
            min_val=min(min_val,node.val)

            left_diff=helper(node.left,max_val,min_val)
            right_diff=helper(node.right,max_val,min_val)
            return max(max_diff,left_diff,right_diff)

        return helper(root,root.val,root.val)
