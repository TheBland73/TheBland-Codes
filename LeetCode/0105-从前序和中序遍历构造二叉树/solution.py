# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        n = len(preorder)

        def build(pre_l: int, pre_r: int, in_l: int, in_r: int) -> TreeNode | None:
            if pre_l >= pre_r:          # 空区间
                return None

            root_val = preorder[pre_l]
            root = TreeNode(root_val)

            # 线性查找根在中序中的位置
            loc = in_l
            while loc < in_r and inorder[loc] != root_val:
                loc += 1

            left_len = loc - in_l       # 左子树节点数

            root.left  = build(pre_l + 1, pre_l + 1 + left_len, in_l, loc)
            root.right = build(pre_l + 1 + left_len, pre_r, loc + 1, in_r)
            return root

        return build(0, n, 0, n)
