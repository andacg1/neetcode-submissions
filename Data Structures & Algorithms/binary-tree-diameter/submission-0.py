# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if node is None:
                return 0
            left = dfs(node.left)   # Get left subtree depth
            right = dfs(node.right) # Get right subtree depth
            # Update diameter: path through current node = left depth + right depth (edges count)
            max_diameter = max(max_diameter, left + right)
            return max(left, right) + 1  # Return current node's depth
        
        dfs(root)
        return max_diameter