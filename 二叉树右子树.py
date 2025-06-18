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
    def rightSideView(self, root):
        ans=[]
        if not root:
            return ans
        queue=[]
        queue.append(root)

        while(queue):
            l=len(queue)
            for i in range(l):
                t=queue.pop(0)
                if t.left:
                    queue.append(t.left)
                if t.right:
                    queue.append(t.right)
                
                if i == l-1:
                    ans.append(t.val)

        return ans

#会慢很多
    # def rightSideView(self, root):
    #     """
    #     :type root: Optional[TreeNode]
    #     :rtype: List[int]
    #     """
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
    #     ans_list=[]
    #     for item in ans:
    #         ans_list.append(item.pop(-1))
        
    #     print(ans_list)

    #     return ans_list

head=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
node3=TreeNode(4)
node4=TreeNode(5)
head.left=node1
head.right=node2
node1.right=node4
node2.right=node3

solu=Solution()
ans=solu.rightSideView(head)
print(ans)
# TreeNode.print_tree_bfs(ans)