import collections  
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    #1 最麻烦的方法，就是挨个遍历，然后存下来每个人的父节点,再去一个中找另一个
    
    #2 遍历的去找每个结点的路径，然后存下来，再对比，其实和上面一个想法
    
    #3 遍历每个结点，找其左右子树中是否存在这俩结点
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None

        #在遍历的过程中，如果当前点是p或者q的其中一个，那么结果必定是这个点，无需继续递归
        if root == p or root == q:
            return root

        #若不是他俩其中一个，那就往左右子树找，直到找到p或者q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        #如果p和q都找到了，那么就说明p和q分别在我的左右子树中，具体在左还是右不一定
        if left and right:
            return root

        #如果只找到了左子树的，那就说明另一个点再左子树中，同理
        return left if left else right
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

p = root.left  # 结点 2
q = root.left.right  # 结点 5

solu=Solution()
lca = solu.lowestCommonAncestor(root, p, q)
print("最近公共祖先是:", lca.val)
    

        


