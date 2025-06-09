class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    #创建新节点（new_node）,这里如果创建，那就是用了n个空间，而我们需要原地排序，所以不可以
    def merge_list(self,head1,head2):
        dummy = ListNode(0)
        tail = dummy

        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1  # 直接链接 head1
                head1 = head1.next
            else:
                tail.next = head2  # 直接链接 head2
                head2 = head2.next
            tail = tail.next
            # new_node=ListNode(0)
            # #或者直接tail.next=head1
            # if head1.val<head2.val:
            #     new_node.val=head1.val
            #     head1=head1.next
            # else:
            #     new_node.val=head2.val
            #     head2=head2.next
            # tail.next=new_node
            # tail=tail.next
        #这里也可以用tail.next=head or head2
        if head1:
            tail.next=head1
        if head2:
            tail.next=head2
        
        
        while tail.next:
            tail = tail.next
        # print(get_ans(dummy.next))
        return dummy.next , tail
    
    def get_len(self,head):
        count=0
        while head:
            head=head.next
            count+=1
        return count

#错误代码  
# def solu(self, head):
#         if not head or head.next==None:
#             return head
#         n=self.get_len(head)
#         size=1
#         cur=start=end=head
#         first=second=head

#         while size<n and cur:
            
#             end=cur
#             #找到第一个链的头和尾,用end找到尾巴，并且断尾
#             count=size
#             while end and count >0:
#                 count-=1
#                 end=end.next
#             second=end.next
#             end.next=None
#             end=second

#             count=size
#             while end and count>0:
#                 count-=1
#                 end=end.next
#             #暂存第二段的下一个链表
#             cur=end.next
#             #断链
#             end.next=None

    def solu(self, head):
        if not head or head.next==None:
            return head
        n=self.get_len(head)
        size=1
        dummy=ListNode(0)
        dummy.next=head

        while size<n:
            #记录每次链表分割的开头
            prev=dummy
            #作为游标，循环链表用
            curr=dummy.next

            while curr:
                #分割第一个链表
                left=curr
                for i in range(size-1):
                    if not curr.next:
                        break
                    curr=curr.next
                #赋值，断链，重新接入游标
                right=curr.next
                curr.next=None
                curr = right

                #分割第二个子链表（如果剩余部分足够）
                if curr:
                    for _ in range(size - 1):
                        if not curr.next:
                            break
                        curr = curr.next
                    #下一轮
                    next_sub = curr.next
                    curr.next = None  # 断链
                    curr = next_sub
                merged_head,merged_tail=self.merge_list(left,right)
                prev.next=merged_head
                prev=merged_tail
                # print(get_ans(dummy.next))
            size *=2
        return dummy.next
                

def get_ans(ans):
    and_list=[]
    while ans:
        and_list.append(ans.val)
        ans = ans.next
    
    return and_list
    



nodeA0 = ListNode(4)
nodeA1 = ListNode(1)
nodeA2 = ListNode(8)
nodeA3 = ListNode(4)
nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
nodeA2.next = nodeA3
nodeA3.next = nodeA4

solution=Solution()
ans=solution.solu(nodeA0)

print(get_ans(ans))
