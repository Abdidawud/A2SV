# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def helper_for_traverse(node):
            result=[]
            while node:
                result.append(node.val)
                node=node.next
            return result

        list_1=helper_for_traverse(l1)
        list_2=helper_for_traverse(l2)

        list_1=list_1[::-1]
        list_2=list_2[::-1]

        ans=int("".join(map(str,list_1)))+int("".join(map(str,list_2)))   
        ans=str(ans)
        
        ans=ans[::-1]

        head=ListNode(ans[0])
        current=head

        for char in ans[1:]:
            new=ListNode(char)
            current.next=new
            current=new
        return head
