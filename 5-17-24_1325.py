'''
1325. Delete Leaves With a Given Value

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, 
it should also be deleted (you need to continue doing that until you cannot).

Submitted on 5-17-24, O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def recurse(root):
            if root == None:
                return None
            if root.left or root.right:
                root.left = recurse(root.left)
                root.right = recurse(root.right) 
            if (not root.left) and (not root.right) and (root.val == target):
                return None
            return root
        return recurse(root)
