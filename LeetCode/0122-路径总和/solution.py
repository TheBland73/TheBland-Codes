# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # dfs-广度优先搜索
        stack = []
        if root == None:
            return False
        stack.append((root,root.val))  #节点+ 计数和 可以在栈上做一些文章

        while stack: #先进后出
            node, cnt = stack.pop()

            if node.right == None and node.left == None:
                if cnt == targetSum:
                    return True

            if node.left != None:
                left = node.left
                stack.append((left,cnt + left.val))
            if node.right != None:
                right = node.right
                stack.append((right,cnt + right.val))
        return False
            
