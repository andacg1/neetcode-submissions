# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        stack = []
        while curr is not None:
            stack.append(curr)
            curr = curr.next
        newHead = stack[-1] if len(stack) > 0 else None
        # print(stack)
        while len(stack) > 0:
            curr = stack.pop()
            if len(stack) > 0:
                curr.next = stack[-1]
            else:
                curr.next = None
        return newHead