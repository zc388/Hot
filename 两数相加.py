class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):


    def solu(self, l1,l2):







        #变慢了，放弃优化，所以最后击败45%
        # start =ListNode(0)  # 创建一个虚拟头节点
        # result=start
        # add = 0

        # while l1 and l2:
            
        #     total = l1.val + l2.val + add
        #     new_node = ListNode(total % 10)
        #     add = total // 10
        #     start.next = new_node
        #     start = start.next
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        
        # while l1:
        #     total=l1.val + add
        #     new_node = ListNode(total % 10)
        #     add = total // 10
        #     start.next = new_node
        #     start = start.next
        #     l1 = l1.next
        # while l2:   
        #     total=l2.val + add
        #     new_node = ListNode(total % 10)
        #     add = total // 10
        #     start.next = new_node
        #     start = start.next
        #     l2 = l2.next    
        
        # if add > 0:
        #     start.next = ListNode(add)
            
        # return result.next

        #速度9ms,试着优化一下，去掉循环中的判断，有一个为none就跳出就行
        # start =ListNode(0)  # 创建一个虚拟头节点
        # result=start
        # add = 0

        # while l1 or l2:
        #     val1 = l1.val if l1 else 0
        #     val2 = l2.val if l2 else 0
            
        #     total = val1 + val2 + add
        #     new_node = ListNode(total % 10)
        #     add = total // 10
        #     start.next = new_node
        #     start = start.next
        #     if l1:
        #         l1 = l1.next
        #     if l2:
        #         l2 = l2.next
        
        # if add > 0:
        #     start.next = ListNode(add)
        # return result.next


        #理解错题意，作者真傻逼，给的例子太有误导性，要么你就别说逆序，要么你就说明白虽然逆序，但是也不用正常加法，而是从前往后加，顺便把list改一下，省得一会儿改
    
        # start =ListNode(0)  # 创建一个虚拟头节点
        # result=start
        # A=list1
        # B=list2

        # lista=[]
        # while list1:
        #     lista.append(list1.val)
        #     list1 = list1.next
        # listb=[]
        # while list2:
        #     listb.append(list2.val)
        #     list2 = list2.next
        
        # lenA = len(lista)
        # lenB = len(listb)
        # if lenA < lenB:
        #     lista = [0] * (lenB - lenA) + lista
        # elif lenB < lenA:
        #     listb = [0] * (lenA - lenB) + listb
                    
        # print(lista)
        # print(listb)
        
        # add=0
        # for  i in range(len(lista)-1,-1,-1):
        #     temp=lista[i] + listb[i]+add
        #     if temp >= 10:
        #         add = 1
        #         temp -= 10
        #     else:
        #         add = 0
        #     new_node = ListNode(temp)
        #     start.next = new_node
        #     start = start.next

        # if add > 0:
        #     new_node = ListNode(add)
        #     start.next = new_node

        # return result.next


    #我这是结果反着输出，人家要正着输出的，循环里倒一下就行
        # A=list1
        # B=list2

        # lista=[]
        # while list1:
        #     lista.append(list1.val)
        #     list1 = list1.next
        # listb=[]
        # while list2:
        #     listb.append(list2.val)
        #     list2 = list2.next
        
        # lenA = len(lista)
        # lenB = len(listb)
        # if lenA < lenB:
        #     lista = [0] * (lenB - lenA) + lista
        # elif lenB < lenA:
        #     listb = [0] * (lenA - lenB) + listb
        
        # add=0
        # for  i in range(len(lista)-1,-1,-1):
        #     temp=lista[i] + listb[i]+add
        #     if temp >= 10:
        #         add = 1
        #         temp -= 10
        #     else:
        #         add = 0
        #     lista[i]=temp

        # if add > 0:
        #     lista.insert(0, add)
        
        # for i in lista:
        #     new_node = ListNode(i)
        #     start.next = new_node
        #     start = start.next

        return result.next
    


nodeA0 = ListNode(2)
nodeA1 = ListNode(4)
nodeA2 = ListNode(9)
# nodeA3 = ListNode(-4)
# nodeA4 = ListNode(5)
nodeA0.next = nodeA1
nodeA1.next = nodeA2
# nodeA2.next = nodeA3
# nodeA3.next = nodeA4

nodeB0 = ListNode(5)
nodeB1 = ListNode(6)
nodeB2 = ListNode(4)
nodeB3 = ListNode(9)
# nodeB4 = ListNode(5)
nodeB0.next = nodeB1
nodeB1.next = nodeB2
nodeB2.next = nodeB3  
# nodeB3.next = nodeB4

solution  =Solution()
ans = solution.solu(nodeA0,nodeB0)
# print(ans)  # 输出 True，因为存在环
while ans:
    print(ans.val)
    ans = ans.next
    
