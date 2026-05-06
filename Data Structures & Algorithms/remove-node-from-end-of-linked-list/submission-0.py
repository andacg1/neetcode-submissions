# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totalLen = 0
        curr = head
        
        while curr:
            totalLen += 1
            curr = curr.next
        # print(totalLen - n)
        if totalLen - n + 1 == 1:
            return head.next
        prev = None
        curr = head
        i = 1
        while curr and i <= totalLen - n:
            prev = curr
            curr = curr.next
            i += 1
        temp_next = curr.next
        if prev:
            prev.next = temp_next
        return head