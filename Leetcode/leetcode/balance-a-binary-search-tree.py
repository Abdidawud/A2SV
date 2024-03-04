# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node):
        if not node:
            return node
        self.inorder(node.left)
        self.li.append(node.val)
        self.inorder(node.right)
    def helper(self, li):
        if len(li)==0:
            return None
        mid=len(li)//2
        root=TreeNode(li[mid])
        root.right=self.helper(li[mid+1:])
        root.left=self.helper(li[:mid])
        return root
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        self.li=[]
        self.inorder(root)
        print (self.li)
        return self.helper(self.li)
        
        