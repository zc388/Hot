"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        new_list=Node(0)
        new_start=new_list
        
        node_dict=dict()
        cur=head
        while cur:
            new_node=Node(cur.val)
            node_dict[cur]=new_node
            new_list.next=new_node
            new_list=new_list.next
            cur=cur.next
        
        # for key,value in node_dict.items():
        #     print(key.val,value.val)

        cur=new_start.next
        while cur:
            cur.random = node_dict.get(head.random)
            cur=cur.next
            head=head.next
        
        cur=new_start.next
        # while cur:
        #     print("cur",cur.val)
        #     if cur.next:
        #         print("cur.next",cur.next.val)
        #     else:
        #         print("cur is end")
        #     if cur.random:
        #         print("cur.random",cur.random.val)
        #     else:
        #         print("cur.random","none")
        #     print("###############")
        #     cur=cur.next
        return cur
        

        

#模拟起来太麻烦，直接在oj写的，写完粘贴过来