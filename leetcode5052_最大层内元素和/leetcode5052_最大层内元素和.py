from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        qTree, q_len, max_sum_val = Queue(), 1, 0
        qTree.put(root)
        level, temp_level = 0, 0
        while not qTree.empty():
            temp_level += 1
            temp, new_len = 0, 0
            for i in range(q_len):
                node = qTree.get()
                temp += node.val
                if node.left:
                    qTree.put(node.left)
                    new_len += 1
                if node.right:
                    qTree.put(node.right)
                    new_len += 1
            q_len = new_len
            if temp > max_sum_val:
                level = temp_level
                max_sum_val = temp
        return level
