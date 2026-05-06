# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        count = 0
        def dfs(node: TreeNode, maxSoFar: int):
            nonlocal count
            if not node:
                return
            if maxSoFar <= node.val:
                count += 1
            dfs(node.left, max(maxSoFar, node.val))
            dfs(node.right, max(maxSoFar, node.val))
        dfs(root, -math.inf)
        return count