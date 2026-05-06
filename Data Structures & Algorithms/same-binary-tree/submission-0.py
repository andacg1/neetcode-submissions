# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def is_same(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left and not right or right and not left:
                return False
            if not left and not right:
                return True
            if left.val != right.val:
                return False
            return is_same(left.left, right.left) and is_same(left.right, right.right)
        return is_same(p, q)