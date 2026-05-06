# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(node: Optional[TreeNode], allowedMin: int, allowedMax: int) -> bool:
            if not node:
                return True
            if node.val <= allowedMin:
                return False
            if node.val >= allowedMax:
                return False
            left_valid = dfs(node.left, allowedMin, min(allowedMax, node.val))
            right_valid = dfs(node.right, max(allowedMin, node.val), allowedMax)
            return left_valid and right_valid
        return dfs(root, -math.inf, math.inf)