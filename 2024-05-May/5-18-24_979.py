'''
979. Distribute Coins in Binary Tree

Difficulty: Medium
Topics: Tree, Depth-First Search, Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. 
There are n coins in total throughout the whole tree.

In one move, 
we may choose two adjacent nodes and move one coin from one node to another. 
A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

Answer from Neetcode, O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node):
            if not node:
                return 0
            leftExtra = dfs(node.left)
            rightExtra = dfs(node.right)
            extra = node.val - 1 + leftExtra + rightExtra
            self.result += abs(extra)
            return extra
        dfs(root)
        return self.result
