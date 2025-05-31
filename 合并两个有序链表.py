class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):


    def solu(self, list1,list2):
        #再次更新，原地插入的思路，还是不行，因为不知道list1的下一个节点是不是比list2的当前节点小，所以还是需要一个新的链表来存储结果
        #并且，在一个循环中，无法控制每次list1和list2的比较顺序都从合适的位置开始，所以可以使用递归的方式！

        if list1 is None:
            return list2   
        if list2 is None:
            return list1
        
        #如果1小，下一个从list1的下一个开始比较合并
        if list1.val <= list2.val:
            list1.next = self.solu(list1.next, list2)
            return list1
        else:
            #如果2小，下一个从list2的下一个开始比较合并
            list2.next = self.solu(list1, list2.next)
            return list2
        
        



        ##########################################################################################################
        #换个思路，原地插入呢，就是只往1种插入，每次比较两个谁大谁小，插入到另一个链表中，并把自己的这个给删了,总共就是n+1次，最后也不用判断了
        #但是这样有个问题，最后没办法返回最长的，因为他们一直再往后连接，那我们就记录一下第一个

        #这样不太行，没办法处理某些情况，例如
        #2，4，5，8 和 1 5 7 

        # if list1 is None and list2 is None:
        #     return None

        #更新，好像可以，当list1小于list2时，可以把list1此时链接到list2上面，然后把list1的下一个节点作为新的list1，继续比较
        #更新，这样也不行，因为不知道list1的下一个的下一个，是不是也小于当前list2的值
        
        # result= list1 if list1.val <= list1.val else list2
        # while list1 and list2:
        #     print(list1.val,list2.val)
        #     if list1.val > list2.val:
        #         temp=list2
        #         list2 = list2.next
        #         temp.next = list1
        #         list1 = temp
        #     else:
        #         list1= list1.next


        #重新搞一个链表
        # strat=result

        # if list1 is None:
        #     return list2
        # if list2 is None:
        #     return list1

        # while list1 and list2:
        #     if list1.val>list2.val:
        #         new_node=ListNode(list2.val)
        #         result.next = new_node
        #         list2= list2.next
        #     else:
        #         new_node=ListNode(list1.val)
        #         result.next = new_node
        #         list1= list1.next
            
        #     result = result.next
        
        # if list1:
        #     result.next = list1
        
        # if list2:
        #     result.next = list2

        # #忽略第一个点
        # strat=strat.next
        # # while strat:
        # #     print(strat.val)
        # #     strat = strat.next

            
        # return result
    


nodeA0 = ListNode(1)
nodeA1 = ListNode(2)
nodeA2 = ListNode(3)
# nodeA3 = ListNode(-4)
# nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
# nodeA2.next = nodeA3
# nodeA3.next = nodeA4

nodeB0 = ListNode(1)
nodeB1 = ListNode(3)
nodeB2 = ListNode(4)
# nodeB3 = ListNode(4)
# nodeB4 = ListNode(5)
nodeB0.next = nodeB1
nodeB1.next = nodeB2
# nodeB2.next = nodeB3  
# nodeB3.next = nodeB4

solution  =Solution()
ans = solution.solu(nodeA0,nodeB0)
# print(ans)  # 输出 True，因为存在环
while ans:
    print(ans.val)
    ans = ans.next
    
