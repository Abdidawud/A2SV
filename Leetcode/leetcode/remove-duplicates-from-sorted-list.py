# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        set_=set()
        current=head
        prev=None

        while current:
            if current.val in set_:
                prev.next=current.next
            else:
                set_.add(current.val)
                prev=current
            current=current.next
        return head