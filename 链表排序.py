class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def get_len(self,head):
        count=0
        while head:
            head=head.next
            count+=1
        return count
    
    def solu(self, head):
        if not head or head.next==None:
            return head
        n=self.get_len(head)
        inter=1
        cur=start=end=head
        while inter<n:
            count=inter
            prew_end=end
            #当次的排序跳inter个，并且第inter个的end也要存在
            while count and end:
                count -=1
                end=end.next
            if count:
                end=prew_end
            
                



        
            inter*=2



        
        

        #递归的做法
        # if not head or not head.next: 
        #     return head
            
        # slow=head
        # fast=head.next
        # left=head
        # #快慢指针，找中间
        # #这里不行了，因为当只有两个值时，这里就不成立了
        # #s=0，f=0
        # #s=1 f=none
        # #进递归，head就是1
        # #s=1,f=1
        # #循环条件失败，再次进入递归
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next

        # mid=slow.next
        # slow.next=None

        # left=self.solu(left)
        # right=self.solu(mid)

        # h=res=ListNode(0)

        # while left and right:
        #     if left.val<right.val:
        #         h.next=left
        #         left=left.next
        #     else:
        #         h.next=right
        #         right=right.next
        #     h=h.next

        # #python 牛逼，直接用or
        # h.next=left or right

        # return res.next
        print()
    


nodeA0 = ListNode(4)
nodeA1 = ListNode(1)
nodeA2 = ListNode(8)
nodeA3 = ListNode(4)
nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
nodeA2.next = nodeA3
nodeA3.next = nodeA4

# while nodeA0:
#     print(nodeA0.val)
#     nodeA0 = nodeA0.next

solution=Solution()
ans=solution.solu(nodeA0)
while ans:
    print(ans.val)
    ans = ans.next
