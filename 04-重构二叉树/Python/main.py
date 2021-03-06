# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。

# 前序遍历序列中，第一个数字总是树的根结点的值。
# 在中序遍历序列中，根结点的值在序列的中间，
# 左子树的结点的值位于根结点的值的左边，
# 而右子树的结点的值位于根结点的值的右边。
# 剩下的我们可以递归来实现

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def reConstructBinaryTree(self,pre,tin):
        if len(pre)==0:
            return None
        elif len(pre)==1:
            return TreeNode(pre[0])
        else:
            root=TreeNode(pre[0])
            pos=tin.index(pre[0])
            root.left=self.reConstructBinaryTree(pre[1:pos+1],tin[:pos])
            root.right=self.reConstructBinaryTree(pre[pos+1:],tin[pos+1:])

        return root