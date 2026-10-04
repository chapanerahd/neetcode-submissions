# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = -float('inf')
        def helper(node):
            if not node:
                return 0


            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)
            path_through_node = (node.val + left_gain + right_gain)
            
            self.ans = max(left_gain + right_gain + node.val, self.ans)
            return max(left_gain, right_gain) + node.val
        
        helper(root)
        return self.ans

