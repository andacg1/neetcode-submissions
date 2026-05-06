# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        def gen():
            num1 = l1
            num2 = l2
            step = 0
            while num1 or num2:
                yield (num1 or ListNode(), num2 or ListNode(), step)
                step += 1
                if num1:
                    num1 = num1.next
                if num2:
                    num2 = num2.next
        nums = gen()
        carry = 0
        
        head = ListNode()
        prev = None
        curr = head
        while res := next(nums, None):
            num1, num2, step = res
            div, mod = divmod(num1.val + num2.val + carry, 10)
            curr.val = mod
            
            curr.next = ListNode()
            prev = curr
            curr = curr.next
            # total += mod
            carry = div
        if carry:
            curr.val = carry
        else:
            prev.next = None
        return head