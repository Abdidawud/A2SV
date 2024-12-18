# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
            
        def helper(node,num):
            if not node:
                return 0
            num= num*10 + node.val

            if not node.left and not node.right:
                return num
            
            left_sum=helper(node.left,num)
            right_sum=helper(node.right,num)
            return (left_sum+right_sum)
        return helper(root,0)