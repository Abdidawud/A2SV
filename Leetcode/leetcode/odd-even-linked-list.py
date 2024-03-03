# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        even_head=ListNode('x')
        odd_head=ListNode('x')
        even=even_head
        odd=odd_head
        cur=head
        i=0
        while cur:
            if i%2==0:
                even.next=cur
                even=even.next
            else:
                odd.next=cur
                odd=odd.next
            cur=cur.next
            i+=1
        odd.next=None
        even.next=None
        even.next=odd_head.next
        return even_head.next