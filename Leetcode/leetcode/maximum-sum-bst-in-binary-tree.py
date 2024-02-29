# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_=0
         

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return [0,0,None,None]
            
            left=traverse(node.left)
            right=traverse(node.right)

            if((left[0]==1 and left[3]<node.val) or left[0]==0) and ((right[0]==1 and right[2]>node.val) or right[0]==0 ):
                sum_=(left[1]+right[1]+node.val)
                self.max_=max(self.max_,sum_)
                left_bound=left[3] if left[3] != None else node.val
                right_bound=right[3] if right[3] != None else node.val
                return[1,sum_,left_bound,right_bound]
            return [2,None,None,None]
        traverse(root)
        return self.max_