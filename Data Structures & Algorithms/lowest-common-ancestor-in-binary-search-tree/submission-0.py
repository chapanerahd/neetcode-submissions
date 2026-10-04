# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def helper(node):

            if not node:
                return 

            if node == p or node == q:
                return node

            is_in_left = helper(node.left)
            is_in_right = helper(node.right)

            if is_in_left and is_in_right:
                return node
            
            return is_in_left or is_in_right

        return helper(root)

