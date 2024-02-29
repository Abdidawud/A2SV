# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        dic=defaultdict(int)
        def helper(node):
            if not node:
                return
            helper(node.left)
            dic[node.val]+=1
            helper(node.right)

        helper(root)
        max_=0
        for i in dic:
            max_=max(max_,dic[i])
        ans=[]
        for i in dic:
            if dic[i]==max_:
                ans.append(i)
        
        print(ans)
        return ans