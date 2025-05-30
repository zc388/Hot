class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def solu(self, headA):
        reverse = None
        prev = None
        while headA:
            next_node = headA.next  
            perv = headA 
            perv.next = reverse  
            reverse = perv
            headA = next_node
        return reverse



        # reverse= None
        # prev = None
        # while headA:
        #     #这里没有保存下一个节点，导致prev.next = reverse后，headA.next会被覆盖
        #     print(headA.val)
        #     prev=headA
        #     prev.next=reverse
        #     reverse=prev
        #     headA= headA.next

        # # while reverse:
        # #     print(reverse.val)
        # #     reverse = reverse.next
        # return prev
    


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