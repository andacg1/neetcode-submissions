"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        copies = {}
        def copyList(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return None
            newNode = Node(x=node.val, next=copyList(node.next), random=node.random)
            copies[node] = newNode
            return newNode
        newHead = copyList(head)
        curr = newHead
        while curr:
            curr.random = copies.get(curr.random)
            curr = curr.next
        return newHead