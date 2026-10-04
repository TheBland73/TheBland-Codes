# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
from typing import Optional
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root == None:
            return []

        d = deque()
        res = []
        d.append(root)
        res.append([root.val])

        while d:
            size = len(d)
            ans = []
            for _ in range(size):
                node = d.popleft()
                if node != None:
                    if node.left != None:
                        d.append(node.left)
                        ans.append(node.left.val)
                    if node.right != None:
                        d.append(node.right)
                        ans.append(node.right.val)
            if ans != []: 
                res.append(ans)
        return res
