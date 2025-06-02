#反转链表+范围

class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution(object):
    #题解的模拟解法，循环时记录开始的head和tail
    # 判断够不够反转，不够的话直接return结果
    # 够的话就对当前的head到tail进行反转，修改一下reverse函数即可，然后再返回新的head和tail，从tail.next开始在记录
    # 比较简单，不写了
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex

        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return hair.next







#############################分别是头插、尾插、以及方便写法######################################### 
    # def solu(self, head, k):
    #     if not head or k==1:
    #         return head
    #     tail=head
    #     #tail指向最后一个当前组的最后一个
    #     for i in range(k-1):
    #         tail=tail.next
    #         if not tail:
    #                 return head
    
    #     tail.next=self.solu(tail.next,k)
        
    #     #尾插法，不断插到尾巴
    #     while head != tail:
    #             temp=head.next
    #             head.next= tail.next
    #             tail.next=head
    #             head=temp
        
    #     return head



#递归！！！这里的方法可以继续优化，比如去掉getLen，即判断相加的次数，如果相加次数小于n，那么就把已经反转的部分再反转回去一次
#或者直接，循环内，如果循环不够数，那就返回head

    # def get_len(self,head):
    #     len=0
    #     while head:
    #         head=head.next
    #         len+=1
        
    #     return len

    # def solu(self, head,n):


    #     #思路没有任何问题，但是问题出在了后面的循环中！
    #     '''
    #     和第一次找尾巴一样，循环停止时后，head会继续等于next，所以循环停止时，已经指向了下一次的头了
    #     所以这里的head.next=self.solu就会直接3指向从3开始的循环，那就出错了
    #     '''
    #     if self.get_len(head)<n:
    #         return head
    #     #先保留一下尾巴，用于找到下一次递归的头
    #     #这里由于是小于2，所以遍历两次之后，就会停止，但是第二次已经指向了第三个值
    #     next_node=head
    #     count=0
    #     while next_node and count<n:
    #         next_node=next_node.next
    #         count+=1
        
    #     count=0
    #     #reverse是链表反转后的起点，此时的head会移动到链表最后
    #     reverse=None
    #     #将n个进行翻转
    #     while head and count<n:
            
    #         temp=head.next
    #         head.next=reverse
    #         reverse=head
    #         if not temp:
    #             break
    #         head=temp
    #         count += 1

    #     start = reverse
    #     while start.next:  # 找到反转部分的最后一个节点
    #         start = start.next

    #     # print("此时替换是的",head.val)
    #     # head.next=self.solu(next_node , n)

    #     start.next = self.solu(next_node, n)
        
    #     return reverse

        '''
    def solu(self, head, n):
        # 如果链表长度小于 n，直接返回
        if self.get_len(head) < n:
            return head

        # 找到第 n+1 个节点，用于后续连接
        next_node = head
        count = 0
        while next_node and count < n:
            next_node = next_node.next
            count += 1

        # 反转前 n 个节点
        reverse = None
        count = 0
        while head and count < n:
            temp = head.next  # 保存下一个节点
            head.next = reverse  # 反转当前节点
            reverse = head  # 更新反转链表的头节点
            head = temp  # 移动到下一个节点
            count += 1

        # 反转后的最后一个节点（原始的 head）需要指向递归反转后的结果
        if reverse:  # 确保 reverse 不为 None
            start = reverse
            while start.next:  # 找到反转部分的最后一个节点
                start = start.next
            start.next = self.solu(next_node, n)  # 连接剩余部分

        return reverse
        '''



n=3
nodeA0 = ListNode(1)
nodeA1 = ListNode(2)
nodeA2 = ListNode(3)
nodeA3 = ListNode(4)
# nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
nodeA2.next = nodeA3
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
ans = solution.reverseKGroup(nodeA0,n)
# print(ans)  # 输出 True，因为存在环
while ans:
    print(ans.val)
    ans = ans.next
    
