# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # queue = deque(root)
        if root is None:
            return []
        queue = deque([root])
        result = []
        while len(queue) > 0:
            result.append(list(map(lambda x: x.val, queue)).copy())
            temp_queue = deque()
            while len(queue) > 0:
                curr = queue.popleft()
                if curr.left:
                    temp_queue.append(curr.left)
                if curr.right:
                    temp_queue.append(curr.right)
            queue = temp_queue
        return result