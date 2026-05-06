# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        if not root:
            return []
        result = [root.val]
        while len(queue) > 0:
            temp_queue = deque()
            while len(queue) > 0:
                curr = queue.popleft()
                if curr.left:
                    temp_queue.append(curr.left)
                if curr.right:
                    temp_queue.append(curr.right)
            if len(temp_queue) > 0:
                result.append(temp_queue[-1].val)
            queue = temp_queue
        return result