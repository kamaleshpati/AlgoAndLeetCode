import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxSumPath:
    def findMaxUtil(self, root, result=-sys.maxsize):
        if root is None:
            return 0, result

        left, result = self.findMaxUtil(root.left, result)

        right, result = self.findMaxUtil(root.right, result)

        result = max(result, root.val)
        result = max(result, root.val + left)
        result = max(result, root.val + right)
        result = max(result, root.val + left + right)

        return max(root.val, root.val + max(left, right)), result

    def maxPathSum(self, root: TreeNode) -> int:
        return self.findMaxUtil(root)[1]
