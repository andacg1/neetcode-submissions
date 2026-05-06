# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        minVal = min(p.val, q.val)
        maxVal = max(p.val, q.val)
        while curr:
            if curr.val <= maxVal and curr.val >= minVal:
                return curr
            if curr.val < minVal:
                curr = curr.right
            elif curr.val > maxVal:
                curr = curr.left