from collections import deque
# Definition for a binary tree node.

#这个题本质上是深搜和广搜的对决！



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #递归的简洁写法
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        #这句是个核心
        return max(left_depth, right_depth) + 1




        #搞个递归的方法
        #错误的递归，每次递归返回时，深度应该加1，不加1的话，每次的返回都会是0，不会记录深度了

        # max_left=0
        # max_right=0
        # if not root:
        #     return 0
        
        # if root.left:
        #     max_left += self.maxDepth(root.left)

        # if root.right:
        #     max_right += self.maxDepth(root.right)

        # max_deep=max(max_left,max_right)

        # return max_deep+1






        # #屌的，直接调用队列，队列元素修改为节点和他的深度
        # if not root:
        #     return 0
        # #([(root, 1)]),外面括号是函数调用，里面中括号代表一个链表，在里面括号代表将节点和数字搞成一个元组
        # queue=deque([(root,1)])
        # max_deep=0

        # while queue:
        #     current,depth=queue.popleft()
        #     if depth>max_deep:
        #         max_deep=depth
            
        #     if current.left:
        #         queue.append((current.left,depth+1))
        #     if current.right:
        #         queue.append((current.right,depth+1))
        # return max_deep



        #迭代list实现，下面用个超标的
        # queue=[root]
        # max_deep=0
        # if not queue:
        #     return max_deep
        
        # while queue:
        #     prev_size=len(queue)
        #     max_deep+=1
        #     #处理每一层
        #     for _ in range(prev_size):
        #         current=queue.pop(0)
        #         if current.left:
        #             queue.append(current.left)
        #         if current.right:
        #             queue.append(current.right)
        
        # return max_deep

        #单纯的bfs，这样写求不了深度
        #因为没办法区分每一层，所以要换一种写法，需要记录当前层的节点数量，然后处理每一层
        # queue=[]
        # current=root
        # max_deep=1

        # if not current:
        #     max_deep = 0

        # while queue or current:

        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)
        #     if len(queue)>max_deep:
        #         max_deep=len(queue)
            
        #     if not queue:
        #         break

        #     current=queue.pop(0)

        # return max_deep




head=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
head.right=node1
node1.left=node2

solu=Solution()
ans=solu.maxDepth(head)
print(ans)