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
    
    def diameterOfBinaryTree(self, root):
        self.ans=1
        def get_length(root):
            if not root:
                return 0
            l_depth=get_length(root.left)
            r_depth=get_length(root.right)

            self.ans=max(self.ans , l_depth+r_depth+1)
            return max(l_depth,r_depth)+1

        get_length(root)
        #因为在这里是点的数量，所以需要减一
        return self.ans-1


    #又错了，答案不一定经过根节点，所以需要在遍历中不断的寻找最合适的点
    # def get_depth(self,root):
    #     if not root:
    #         return 0
        
    #     #这里算的其实是点的数量，而不是路径的数量，这个题目中，路径的意思是两点之间的路径
    #     l_depth=self.get_depth(root.left)
    #     r_depth=self.get_depth(root.right)
    #     #但是在这里深度还需要加1，因为又走了一层
    #     return max(l_depth,r_depth)+1
    
    # def diameterOfBinaryTree(self, root):
    #     if not root:
    #         return 0
        
    #     l_depth=self.get_depth(root.left)
    #     print(l_depth)
    #     r_depth=self.get_depth(root.right)
    #     print(r_depth)
    #     return l_depth+r_depth





        #错误思想，以为深度或者最宽宽度就是节点路径，非常错误的想法！
        #路径和节点有关系，可转化为求左右子树的最大长度（深度）
        # if not root:
        #     return 0
        
        # max_width=0
        # max_high=0
        
        # queue=deque([(root,1)])
        # while(queue):
        #     width=len(queue)
        #     if width>max_width:
        #         max_width=width

        #     current,high=queue.popleft()
        #     if high>max_high:
        #         max_high=high

        #     if current.left:
        #         queue.append((current.left,high+1))
        #     if current.right:
        #         queue.append((current.right,high+1))
    
        # if max_width>max_width:
        #     return max_width-1
        # else:
        #     return max_high-1





head = TreeNode(4)
node1 = TreeNode(-7)
node2 = TreeNode(-3)
node3 = TreeNode(-9)
node4 = TreeNode(-3)
node5 = TreeNode(9)
node6 = TreeNode(-7)
node7 = TreeNode(-4)
node8 = TreeNode(6)
node9 = TreeNode(-6)
node10 = TreeNode(-6)
node11 = TreeNode(0)
node12 = TreeNode(6)
node13 = TreeNode(5)
node14 = TreeNode(9)
node15 = TreeNode(-1)
node16 = TreeNode(-4)
node17 = TreeNode(-2)

# 构建树的连接关系
head.left = node1
head.right = node2

node2.left = node3
node2.right = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node6.left = node9
node6.right = node10

node8.left = node11
node8.right = node12

node10.left = node13
node10.right = node14

node12.left = node15
node12.right = node16

node14.right = node17


solu=Solution()
ans=solu.diameterOfBinaryTree(head)
print(ans)
# TreeNode.print_tree_bfs(ans)