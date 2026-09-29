# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #从遍历二叉树到底部
        #优先遍历右子树，如果没有，再去遍历左子树
        #比较合适的是采用 广度优先遍历-BFS
        
        res = []
        if not root:
            return res
        d = deque()
        d.append(root)
        res.append(root.val)

        #确定每层处理，通过统计处理前每层的节点数进行实现
        while d:
            size = len(d)
            for _ in range(size):
                node = d.popleft()
                if node != None and node.left:
                    d.append(node.left)
                if node != None and node.right:
                    d.append(node.right)
            if d:  #非空
                res.append(d[-1].val)

        return res    
