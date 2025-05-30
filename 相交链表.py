# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = set()
        while headA:
            visited.add(headA)
            headA = headA.next

        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next

        return None

        # while headA and headB:
        #     print(headA.val, headB.val)
        #     if headA.val == headB.val:
        #         return f"Intersected at {headA.val}"
        #     headA = headA.next
        #     headB = headB.next
        # return None
    


nodeA0 = ListNode(4)
nodeA1 = ListNode(1)
nodeA2 = ListNode(8)
nodeA3 = ListNode(4)
nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
nodeA2.next = nodeA3
nodeA3.next = nodeA4

# nodeB0 = ListNode(5)
# nodeB1 = ListNode(6)
# nodeB2 = ListNode(8)
# nodeB3 = ListNode(4)
# nodeB4 = ListNode(5)
# nodeB0.next = nodeB1
# nodeB1.next = nodeB2
# nodeB2.next = nodeB3  
# nodeB3.next = nodeB4


solu=Solution()
ans=solu.getIntersectionNode(nodeA0, nodeB0)
if ans:
    print("Intersection found at node with value:", ans.val)
else:
    print("No intersection")

# # while node1:
# #     print(node1.val)
# #     node1 = node1.next

# node0=ListNode(0)
# node0.next = node1

# # while node0:
# #     print(node0.val)
# #     node0 = node0.next

# #删除值为1的
# #定义一下开头
# current = node0

# prev=None

# #当前指针存在，且值不为1
# while current and current.val != 1:
#     prev = current
#     current = current.next

# if current:
#     #如果有前一个点
#     if prev:
#         prev.next = current.next
#     #如果没钱一个点，即这个点是开头的话
#     else:
#         node0 = current.next

# while node0:
#     print(node0.val)
#     node0 = node0.next