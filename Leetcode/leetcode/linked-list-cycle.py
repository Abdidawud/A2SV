# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rabbit=head
        tortoise=head
        flag=False
        while rabbit and rabbit.next:
            rabbit=rabbit.next.next
            tortoise=tortoise.next
            if rabbit==tortoise:
                flag=True
                break
        if flag:
            return True
        else:
            return False