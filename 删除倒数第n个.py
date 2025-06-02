class ListNode(object):
    def __init__(self, x,next=None):
        self.val = x
        self.next = next

class Solution(object):

    def get_len(self,head):
        len=0
        while head:
            head=head.next
            len+=1
        
        return len

#题解的方法跟我差不多，只不过写法不一样，而且更加科学，哈哈哈哈
    # def getLength(head: ListNode) -> int:
    #     length = 0
    #     while head:
    #         length += 1
    #         head = head.next
    #     return length
    
    # dummy = ListNode(0, head)
    # length = getLength(head)
    # cur = dummy
    # for i in range(1, length - n + 1):
    #     cur = cur.next
    # cur.next = cur.next.next
    # return dummy.next

    def solu(self, head,n):
        #聪明方法，可以用双指针
        #快慢指针牛逼！快比慢，要快n，这样的话当快指针到达末尾时，慢指针正好是倒数第n个，牛批
        start=ListNode(0,head)

        #这个地方我一开始写的是slow=slow.next，fast同理，但其实是错误的！
        #因为我没意识到序号不对齐，并且这样子写的话，当只有一个数字，并且需要删除那唯一的数，fast直接指向了none，slow不会指向别的，所以其实并没有删除
        slow=start
        fast=start
        #fast先走n个
        for i in range(n):
            fast=fast.next
        
        #预定义一个prew
        prew=slow
        while fast:
            prew=slow
            fast=fast.next
            slow=slow.next
        
        prew.next=prew.next.next
        
        return start.next


        












#############################################################################################################################
        #栈！！！！先进后出，完美啊哥们，就是不知道python的栈咋实现，发现list一样，弹出即可


        #这里很巧妙，初始化了一个节点，这个是个空结点，当内容为空时这个就代表链表，同时遍历时也不会造成为stack为none的情况！
        start=ListNode(0,head)
        stack=list()
        cur=start
        #这里要便利start，因为节点加入了一个头节点，遍历head就不对了，我就错在这儿！
        while cur:
            stack.append(cur)
            cur=cur.next
        
        for i in range(0,n):
            stack.pop()
        
        #取出当前的栈顶元素
        prev=stack[-1]
        prev.next=prev.next.next
        return start.next

#############################################################################################################################
        # current=head
        # prew=head
        # len=self.get_len(head)

        # if n==len  :
        #     return current.next

        # for i in range(0, (len-n)):
        #     #保存上一个
        #     prew=head
        #     head=head.next
        
        # prew.next=head.next
        # return current




n=1
nodeA0 = ListNode(1)
nodeA1 = ListNode(2)
# nodeA2 = ListNode(9)
# nodeA3 = ListNode(-4)
# nodeA4 = ListNode(5)
nodeA0.next = nodeA1
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
ans = solution.solu(nodeA0,n)
# print(ans)  # 输出 True，因为存在环
while ans:
    print(ans.val)
    ans = ans.next
    
