class Solution:
    def inorderSuccessor(self, root, x):
        if root is None:
            return None
        ans=None
        while root:
            if root .data > x.data:
                ans=root
                root=root.left
            else:
                root=root.right
        return ans
