from functools import cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        @cache
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        def traverse(node: Optional[TreeNode]) -> bool:
            # nonlocal balanced
            # if not balanced:
            #     return False
            if not node:
                return True
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) > 1:
                # balanced = False
                return False
            return traverse(node.left) and traverse(node.right)
        return traverse(root)