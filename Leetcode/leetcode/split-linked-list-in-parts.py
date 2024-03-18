# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        dummy=head
        count=0
        while dummy:
            count+=1
            dummy=dummy.next
        res=[]
        size=count//k
        larger_count=count%k
        for i in range(k):
            part=head
            length=size + (1 if larger_count >0 else 0)
            larger_count-=1

            for _ in range(length-1):
                if head:
                    head=head.next
            if head:
                next_=head.next
                head.next=None
                head=next_
            res.append(part)
        return res
