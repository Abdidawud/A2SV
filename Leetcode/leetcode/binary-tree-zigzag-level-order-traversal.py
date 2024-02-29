# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result=[]
        queue=deque([root])
        direction=1  #use 1 for right to left use -1 for left to right traversal
        
        while queue:
            level_stack=[]
            level_size=len(queue)

            for i in range(level_size):
                node=queue.popleft()
                level_stack.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if direction==-1:
                level_stack.reverse()
            result.append(level_stack)
            direction *=-1
        return result