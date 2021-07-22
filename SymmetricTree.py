# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSame(self,root1,root2):
        if not root1 or not root2:
            return root1==root2
        if root1.val!=root2.val:
            return False
        return self.isSame(root1.left,root2.right) and self.isSame(root1.right,root2.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSame(root.left,root.right)
