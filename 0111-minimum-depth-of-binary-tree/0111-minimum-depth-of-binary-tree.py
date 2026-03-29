# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        #If left mai kuch nai hai
        if not root.left:
            return 1 + self.minDepth(root.right)
        #If right mai kuch nai hai 
        if not root.right:
            return 1 + self.minDepth(root.left)
        #If dono mai kuch na kuch hai then just search for the minimum in the both
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))