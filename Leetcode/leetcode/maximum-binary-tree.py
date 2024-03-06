# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(li):
            max_=-float('inf')
            index_=0
            for i in range(len(li)):
                if max_<li[i]:
                    max_=li[i]
                    index_=i
            if li==[]:
                return None
            root=TreeNode(max_)
            root.right=recurse(li[index_+1:])
            root.left=recurse(li[:index_])
            return root
        return recurse(nums)