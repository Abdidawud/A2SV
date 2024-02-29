# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_than_x = ListNode(0)
        greater_than_or_equal_to_x = ListNode(0)
        
        less_tail = less_than_x
        greater_or_equal_tail = greater_than_or_equal_to_x
        
        while head:
            if head.val < x:
                less_tail.next = head
                less_tail = less_tail.next
            else:
                greater_or_equal_tail.next = head
                greater_or_equal_tail = greater_or_equal_tail.next
            
            head = head.next
        
        less_tail.next = greater_than_or_equal_to_x.next
        greater_or_equal_tail.next = None
        
        return less_than_x.next
