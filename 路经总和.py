from collections import deque
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def dfs(self,root,targetSum):
        if not root:
            return 0
        res=0

        if root.val == targetSum:
            res += 1

        res+=self.dfs(root.left,targetSum-root.val)
        res+=self.dfs(root.right,targetSum-root.val)

        return res



    def pathSum(self, root, targetSum):
        if not root:
            return 0
        
        res=self.dfs(root,targetSum)
        #这里SB了，因为从其他节点开始的话，也必须保证结果等于8！！！
        res+=self.pathSum(root.left , targetSum)
        res+=self.pathSum(root.right , targetSum)
        
        return res



#遍历所有的路径，直接记录下来总和
#当前的想法，单词递归不可以，只能求出所有从根节点出发的满足条件的路径，而从其他结点出发的没法儿求出来

    # def pathSum(self, root, targetSum):
    #     if not root:
    #         return 0
        
    #     def dfs(root,targetSum):
    #         if not root:
    #             return 0
    #         res=0

    #         if root.val == targetSum:
    #             res += 1

    #         res+=dfs(root.left,targetSum-root.val)
    #         res+=dfs(root.right,targetSum-root.val)

    #         return res
        
    #     ans=dfs(root,targetSum)


head=TreeNode(3)
node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(5)
head.left=node1
head.right=node3
node1.right=node2

preorder = [3,9,20,15,7],
inorder = [9,3,15,20,7]
solu=Solution()
ans=solu.pathSum(preorder,inorder)

print(ans)