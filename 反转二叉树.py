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
    #深搜递归
    def invertTree(self, root):
        if not root:
            return None
        if root.left:
            root.left=self.invertTree(root.left)
        if root.right:
            root.right=self.invertTree(root.right)
        
        root.left,root.right=root.right,root.left
        
        return root


        #=广搜
        # if not root:
        #     return None
        
        # queue=deque([(root,1)])
        # while queue:
        #     current,size=queue.popleft()

        #     for _ in range(size):
        #         size -= 1
        #         current.left,current.right=current.right,current.left
        #         if current.left:
        #             queue.append((current.left,size+1))
        #         if current.right:
        #             queue.append((current.right,size+1))

        # return root




head=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
head.right=node1
node1.left=node2

solu=Solution()
ans=solu.invertTree(head)

TreeNode.print_tree_bfs(ans)