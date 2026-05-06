from heapq import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        heap = []
        def dfs(node: Optional[TreeNode]):
            nonlocal heap
            if not node:
                return
            heappush_max(heap, node.val)
            while len(heap) > k:
                heappop_max(heap)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return max(heap)