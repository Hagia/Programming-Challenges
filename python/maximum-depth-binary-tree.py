# Definition for a binary tree node.
from turtle import right

## Taken from leetcode.com
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):

        if root == None:
            return 0
        
        left_count = 1 + self.maxDepth(root.left)
        right_count = 1 + self.maxDepth(root.right)
        
        return max(right_count, left_count)