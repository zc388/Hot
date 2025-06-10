from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #递归写法，但是这里要求有返回一个列表
    # def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
    #     if root:
    #         if root.left:
    #             self.inorderTraversal(root.left)

    #         print(root.val)

    #         if root.right:
    #             self.inorderTraversal(root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans=[]
        if not root:
            return ans
        
        stack=[]
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current=current.left

            current = stack.pop()
            ans.append(current.val)

            current=current.right

        return ans
            
            





head=TreeNode(1)
node1=TreeNode(2)
node2=TreeNode(3)
head.right=node1
node1.left=node2

solu=Solution()
ans=solu.inorderTraversal(head)
print(ans)