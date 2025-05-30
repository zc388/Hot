class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # def list_len(self, headA):
    #     count = 0
    #     while headA:
    #         count += 1
    #         headA = headA.next
    #     return count

    def reverse(self, headA):
        reverse = None
        while headA:
            next_node = headA.next  
            headA.next = reverse  
            reverse = headA
            headA = next_node
        return reverse
    
    #这个思想很重要，快慢指针，当快指针走到末尾时，慢指针刚好走到中间
    # 这个函数可以用来找到链表的中点
    def end_of_first_half(self, headA):
        fast = headA
        slow = headA
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow


    def isPalindrome(self, head):
        if head is None:
            return True
        #想一下空间On的解法
        #找一下链表的中点，然后将后半部分反转，再和前半部分进行比较
        result = True
        first_half_node = self.end_of_first_half(head)
        #反转后的链表,即后半段的倒序
        second_half_start = self.reverse(first_half_node.next)

        #将前半部分的链表断开
        while second_half_start :
            if head.val != second_half_start.val:
                result = False
            head = head.next
            second_half_start = second_half_start.next

        return result








        # #还有更吊的，直接进行正反判断，即，将数组反过来是否仍然一样
        # vals = []
        # current_node = head
        # while current_node is not None:
        #     vals.append(current_node.val)
        #     current_node = current_node.next
        # return vals == vals[::-1]


        #存列表里
        # head=[]
        # while headA:
        #     head.append(headA.val)
        #     headA = headA.next
        # len_head = len(head)
        # for i in range(len_head // 2):
        #     if head[i] != head[len_head - 1 - i]:
        #         return False
        # return True

nodeA0 = ListNode(1)
nodeA1 = ListNode(2)
nodeA2 = ListNode(2)
nodeA3 = ListNode(1)
# nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
nodeA2.next = nodeA3
# nodeA3.next = nodeA4

# while nodeA0:
#     print(nodeA0.val)
#     nodeA0 = nodeA0.next

solution=Solution()
ans=solution.isPalindrome(nodeA0)
print(ans)