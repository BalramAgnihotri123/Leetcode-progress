# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxDiameter = 0
        
        def height(root):
            if not root:
                return 0
            
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            self.maxDiameter = max(self.maxDiameter, leftHeight + rightHeight)
            return 1 + max(leftHeight, rightHeight)

        height(root)
        return self.maxDiameter