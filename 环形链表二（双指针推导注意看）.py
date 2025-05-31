class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def getnum(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count


    def solu(self, head):
        if not head or not head.next:
            return None

        #双指针方法，就有点牛逼，需要多看
        packup=head
        fast=head.next
        slow=head
        #此时，如果跳出循环，就代表二者相遇了，这时候再找一个从头开始走，再与慢指针相遇的地方就是环的起点
        while fast != slow:
            if not fast or not fast.next:
                return None  
            fast = fast.next.next
            slow = slow.next
        
        while packup != slow:
            packup = packup.next
            slow = slow.next   
        return packup
        





        #和上一个题一样，可以用set优化时间
        result=None
        result = False
        visited = []
        while head:
            if head in visited:
                result = True
                break
            visited.append(head)
            headA = head.next





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
    
