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


    #题解是迭代写法，我直接粘贴过来
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    #我忽略了题目，题目说到，这是一个搜索树，搜索树是左小于右的树，所以是有规律的
    #而中序遍历正好满足，所以可以直接中序遍历一遍
    # #递归写法
    # def kthSmallest(self, root , k):
    #     if not root:
    #         return None
    #     ans=[]
    #     def middle_order(root,ans):
    #         if not root:
    #             return None
    #         if root.left:
    #             middle_order(root.left,ans)
            
    #         ans.append(root.val)

    #         if root.right:
    #             middle_order(root.right,ans)
        
    #     middle_order(root,ans)

    #     return ans[k-1]



    # #广搜再排序
    # def kthSmallest(self, root,k):
    #     if not root:
    #         return None
        
    #     ans=[]
        
    #     queue=deque([(root,1)])
    #     while queue:
    #         current,size=queue.popleft()
    #         ans.append(current.val)

    #         for _ in range(size):
    #             size -= 1
    #             if current.left:
    #                 queue.append((current.left,size+1))
    #             if current.right:
    #                 queue.append((current.right,size+1))
        
    #     ans.sort()
    #     return ans[k-1]




head=TreeNode(3)
node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(5)
head.left=node1
head.right=node3
node1.right=node2

solu=Solution()
ans=solu.kthSmallest(head,1)

TreeNode.print_tree_bfs(ans)