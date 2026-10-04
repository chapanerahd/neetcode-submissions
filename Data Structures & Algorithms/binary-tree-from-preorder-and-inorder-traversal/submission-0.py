# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        num_to_idx = {num: idx for idx, num in enumerate(inorder)}
        preorder = deque(preorder)
        def helper(left, right):
            if left > right:
                return
            
            val = preorder.popleft()
            node = TreeNode(val)
            node.left = helper(left, num_to_idx[val] - 1)
            node.right = helper(num_to_idx[val] + 1, right)
            return node
        
        return helper(0, len(preorder) - 1)
            
        