# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        
        mid = head
        tail = mid.next
        while tail is not None:
            mid = mid.next
            tail = tail.next
            tail = tail.next if tail is not None else None
        

        curr = mid
        prev = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        

        def gen():
            node1 = head
            node2 = prev
            while node1 or node2:
                yield node1
                node1 = node1.next
                yield node2
                node2 = node2.next
        ctr = gen()
        curr = next(ctr)
        
        while curr:
            curr.next = next(ctr)
            curr = curr.next