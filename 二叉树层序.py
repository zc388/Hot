from collections import deque
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree_bfs(root):
        if not root:
            return
        queue = deque([root])
        while queue:
            level_size = len(queue)  # 当前层的节点数
            level_nodes = []  # 当前层的节点值
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    level_nodes.append(node.val)
                    queue.append(node.left)  # 添加左子节点
                    queue.append(node.right)  # 添加右子节点
                else:
                    level_nodes.append(None)  # 空节点用 None 表示

            # 打印当前层的节点值
            print(level_nodes)

class Solution(object):

    def levelOrder_dfs(self,root):
        if not root:
            return []
        self.ans=[]
        self.dfs(root,1)

        return self.ans
    
    #深搜,由于普通深搜没办法记录深度，所以在这里需要带入递归的深度以判断当前结点属于第几层
    def dfs(self,root,high):

        if len(self.ans)<high:
            self.ans.append([])

        self.ans[high-1].append(root.val)

        if root.left:
            self.dfs(root.left,high+1)
        if root.right:
            self.dfs(root.right,high+1)



    # #广搜
    # def levelOrder(self, root):
    #     ans=[]
    #     if not root:
    #         return ans
    #     queue=deque([root])
    #     ans.append([root.val])
    #     while queue:
    #         size=len(queue)
    #         level=[]
    #         print(size)
    #         for _ in range(size):
    #             current=queue.popleft()
    #             if current.left:
    #                 queue.append(current.left)
    #                 level.append(current.left.val)
    #             if current.right:
    #                 queue.append(current.right)
    #                 level.append(current.right.val)
            
    #         if level:
    #             ans.append(level)
    #     return ans

        


head=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
head.right=node1
node1.left=node2

solu=Solution()
ans=solu.levelOrder_dfs(head)
print(ans)
# TreeNode.print_tree_bfs(ans)