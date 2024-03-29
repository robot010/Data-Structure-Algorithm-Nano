# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return

        if key>root.val:
            root.right = self.deleteNode(root.right, key)
        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.left:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

        return root

    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right

        return root.val

    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left

        return root.val
