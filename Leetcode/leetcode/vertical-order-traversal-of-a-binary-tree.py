# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic=defaultdict(list)
        def helper_func(node,col,row):
            nonlocal dic
            if not node:
                return
            dic[(col,row)].append(node.val)
            helper_func(node.left,col-1,row+1)
            helper_func(node.right,col+1,row+1)
        helper_func(root,0,0)

        sort_dic=sorted(dic.items(),key=lambda x:x[0])
        print(sort_dic)

        offset=0
        max_=0

        
        for i in sort_dic:
            offset=min(offset,i[0][0])
            max_=max(max_,i[0][0])
            i[1].sort()
        ans=[ []for i in range(max_ - offset+1)]

        for i in sort_dic:
            ans[i[0][0]-offset].extend(i[1])
        return ans        