class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):


    def solu(self, head):

        #这是题解
        result = False
        if not head or not head.next:
            return result
        # 使用快慢指针来判断是否有环，o(n)时间复杂度，o(1)空间复杂度
        
        fast=head.next
        slow=head

        while fast != slow:
            if not fast or not fast.next:
                result = False
                return result
            fast = fast.next.next
            slow = slow.next
        
        result = True

        #这个也可以
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow :
        #         result = True
        #         break


        #用set会更快
        # result = False
        # visited = set()
        # while head:
        #     if head in visited:
        #         result = True
        #         break
        #     visited.add(head)
        #     head = head.next

        #用list比较慢
        # result = False
        # visited = []
        # while headA:
        #     if headA in visited:
        #         result = True
        #         break
        #     visited.append(headA)
        #     headA = headA.next

        return result
    


nodeA0 = ListNode(3)
nodeA1 = ListNode(2)
nodeA2 = ListNode(0)
nodeA3 = ListNode(-4)
# nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
nodeA2.next = nodeA3
# nodeA3.next = nodeA4

solution  =Solution()
ans = solution.solu(nodeA0)
print(ans)  # 输出 True，因为存在环
    
