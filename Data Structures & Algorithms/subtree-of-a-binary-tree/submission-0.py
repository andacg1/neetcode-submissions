# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left and right or left and not right:
                return False
            if left.val != right.val:
                return False
            return is_same(left.left, right.left) and is_same(left.right, right.right)
        
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            matches = is_same(node, subRoot)
            if matches:
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)