# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self,node):
        if not node:
            return 0
        leftht=self.height(node.left)
        rightht=self.height(node.right)
        if leftht==-1 or rightht==-1 or abs(leftht-rightht) > 1:
            return -1
        
        return 1 + max(self.height(node.left),self.height(node.right))
            
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        #if height of leftsubtree and rightsubtree > 1 then it is not balanced
        return self.height(root)!=-1
