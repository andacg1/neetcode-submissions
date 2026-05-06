"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        # root = Node(val=node.val)
        cloned = {}
        def clone(original_node: Optional['Node']) -> Optional['Node']:
            if not original_node:
                return None
            if original_node.val in cloned.keys():
                return cloned[original_node.val]
            new_node = Node(val=original_node.val)
            cloned[original_node.val] = new_node
            #new_node.neighbors
            for neighbour in original_node.neighbors:
                new_node.neighbors.append(clone(neighbour))
            return new_node
        return clone(node)