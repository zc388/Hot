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

'''
在 inorder 中找到 mid 为根节点的下标
由于中序遍历特性，mid 左侧都为左子树节点，所以左子树的节点有 mid 个
那么同样的，由于前序遍历的特性，preorder 第一个元素（根节点）后跟着的就是它的左子树节点，一共有 mid 个，所以切了 [1:mid+1] 出来
'''
class Solution(object):

    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])

        #第一个是前序，第二个是中序
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])

        root.right=self.buildTree(preorder[index+1:] , inorder[index+1:])

        
        print("This is a placeholder for the buildTree method.")


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
ans=solu.buildTree(preorder,inorder)

TreeNode.print_tree_bfs(ans)