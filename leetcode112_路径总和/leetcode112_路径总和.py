# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == s
        return self.hasPathSum(root.left, s - root.val) or self.hasPathSum(root.right, s - root.val)
        