from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
    # 用队列或栈保存“应该互为镜像的节点对”。
    # 初始放入 (root.left, root.right)。每次取出一对 (a, b)：
    # 都为空：继续；
    # 一个为空或值不同：返回 false；
    # 否则按镜像顺序压入下一对：
    # (a.left, b.right)
    # (a.right, b.left)
    # 全部比较完没矛盾，就是对称。
        d = deque()
        d.append((root.left,root.right))
        # 入队和出队 应为一对镜像节点
        while d:  # 0-左 1-右
            a,b = d.popleft()
            if a == None and b == None:
                continue
            if a is None or b is None or a.val != b.val:
                return False
            d.append((a.left,b.right))
            d.append((a.right,b.left))

        return True
