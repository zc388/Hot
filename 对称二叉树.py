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
    def check(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        #这里判断传入的俩一不一样
        is_euql=(left.val==right.val)

        #self.check(left.left,left.righr) and self.check(right.left,right.right)这里不对，有问题，应该是判断左右子树的对称位置，而不是判断当前节点的左右孩子
        #应该是左子树的左孩子和右子树的有孩子进行比对
        return  is_euql and self.check(left.right,right.left) and self.check(left.left,right.right)
    
    def isSymmetric(self, root):

        return self.check(root.left,root.right)

        



        #广搜
        # queue=deque([root])
        
        # #按层存储所有节点
        # while queue:
        #     size=len(queue)
        #     node=[]
        #     for _ in range(size):
        #         current=queue.popleft()
        #         if current:
        #             node.append(current.val)
        #             queue.append(current.left)
        #             queue.append(current.right)
        #         else:
        #             node.append(None)

        #     ##按层进行对称检测
        #     for i in range(len(node)//2):
        #         if node[i] != node[len(node)-i-1]:
                    
        #             return False

        # return True




head=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
head.right=node1
node1.left=node2

solu=Solution()
ans=solu.isSymmetric(head)
print(ans)
# TreeNode.print_tree_bfs(ans)