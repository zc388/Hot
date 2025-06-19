from collections import deque


class TreeNode:
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

class Solution:


    def flatten(self, root):

        if not root:
            return ans
        ans=[]
        def dfs(root,ans):
            if not root:
                return None
            
            ans.append(root)
            if root.left:
                dfs(root.left,ans)
            if root.right:
                dfs(root.right,ans)
        
        dfs(root,ans)
        
        for i in range(len(ans)-1):
            current=ans[i]
            current.right=ans[i+1]
            current.left=None

        return ans[0]            
            





head=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
head.right=node1
node1.left=node2

solu=Solution()
ans=solu.flatten(head)
TreeNode.print_tree_bfs(ans)