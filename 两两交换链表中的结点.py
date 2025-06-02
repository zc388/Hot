class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution(object):
    #题解，直接判断条件多加一个，不用额外求时间了
    # def swapPairs(self, head: ListNode) -> ListNode:
    #     dummyHead = ListNode(0)
    #     dummyHead.next = head
    #     temp = dummyHead
    #     while temp.next and temp.next.next:
    #         node1 = temp.next
    #         node2 = temp.next.next
    #         temp.next = node2
    #         node1.next = node2.next
    #         node2.next = node1
    #         temp = node1
    #     return dummyHead.next


    def get_len(self,head):
        len=0
        while head:
            head=head.next
            len+=1
        
        return len

    def solu(self, head):
        #这里想错了，应该是当前的小链表中没节点，或者没下一个节点
        # if not head.next or not head.next.next:
        #     return head

        if not head or not head.next:
            return head
        temp=head.next
        #交换后的需要指向下一块链表
        head.next=self.solu(temp.next)
        temp.next=head

        #因为交换后，temp，即原来的后面的head.next就变成了当前链表的最开始的头
        return temp

        #这玩意迭代
        # start=ListNode(0,head)
        # cur=start.next
        # prew=start

        # len=self.get_len(cur)
        # if(len==1 or len == 0):
        #     return head

        # while cur.next:
        #     #交换顺序
        #     #0 1 2 3  变  0  (不连接)   2 1 3
        #     temp=cur.next
        #     cur.next=cur.next.next
        #     temp.next=cur

        #     #和之前的串链接，更新前一个串的最后一个值为当前处理的值（即交换值）
        #     #0->2
        #     prew.next=temp
        #     prew=cur
        #     if not cur.next:
        #         break
        #     cur=cur.next
        
        # return start.next




n=1
nodeA0 = ListNode(1)
nodeA1 = ListNode(2)
nodeA2 = ListNode(3)
nodeA3 = ListNode(4)
# nodeA4 = ListNode(5)
# nodeA0.next = nodeA1
# nodeA1.next = nodeA2
# nodeA2.next = nodeA3
# nodeA3.next = nodeA4

# nodeB0 = ListNode(5)
# nodeB1 = ListNode(6)
# nodeB2 = ListNode(4)
# nodeB3 = ListNode(9)
# nodeB4 = ListNode(5)
# nodeB0.next = nodeB1
# nodeB1.next = nodeB2
# nodeB2.next = nodeB3  
# nodeB3.next = nodeB4

solution  =Solution()
ans = solution.solu(None)
# print(ans)  # 输出 True，因为存在环
while ans:
    print(ans.val)
    ans = ans.next
    
