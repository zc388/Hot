class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache():

    def __init__(self, capacity:int):
        """
        :type capacity: int
        """
        self.cache = dict()
        # 使用伪头部和伪尾部节点
           
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        # 初始化 
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key:int):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        #字典存储的是key和对应的节点
        #在字典中先找到这个node，再挪到开头
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key:int, value:int):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            node=DLinkedNode(key,value)
            #这里无需考虑重复的事
            self.cache[key]=node
            self.addToHead(node)
            self.size+=1
            #这一段代码值得记录与思考,题解这么写能过，我自己这么写为什么过不了？
            #因为get那里，sb写成了addtohead，应该是move！
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def removeNode(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def addToHead(self, node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node=self.tail.prev
        self.removeNode(node)
        #返回一下删除了的值
        return node
    
#力扣的超标做法
# import collections
# class LRUCache(collections.OrderedDict):

#     def __init__(self, capacity: int):
#         super().__init__()
#         self.capacity = capacity


#     def get(self, key: int) -> int:
#         if key not in self:
#             return -1
#         self.move_to_end(key)
#         return self[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self:
#             self.move_to_end(key)
#         self[key] = value
#         if len(self) > self.capacity:
#             self.popitem(last=False)


# 超时，虽然是O(n)
# class LRUCache(object):

#     def __init__(self, capacity):
#         """
#         :type capacity: int
#         """
#         self.memory=dict()
#         self.max_size=capacity
#         self.lru=dict()
        

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         #那么在这儿就要处理谁该被替换
#         max=0
#         if key in self.memory:
#             #当前所处的位置，后面要进行变化的
#             temp=self.lru.get(key)
#             for key_,value_ in self.lru.items():
#                 #但凡是在交换前，排序在前面的，序号都要降低一位。如果在后面的，序号不需要变化
#                 if value_>max:
#                     max=value_

#                 if value_>temp:
#                     self.lru[key_]=value_-1
                
#             self.lru[key]=max

#             print(f"######查询了{key}########")
#             for key_,value_ in self.lru.items():
#                 print(f"{key_,value_}",end=" ")
#             print()
#             print("#############")

#             return self.memory.get(key)
        
#         print(f"######查询了{key}，但是没查到########")
#         for key_,value_ in self.lru.items():
#             print(f"{key_,value_}",end=" ")
#         print()
#         print("#############")

#         return -1
        

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         #已存在，更换一下值，再换一下序号
#         if key in self.memory:
#             max=0
#             self.memory[key]=value
#             #当前所处的位置，后面要进行变化的
#             temp=self.lru.get(key)
#             for key_,value_ in self.lru.items():
#                 #但凡是在交换前，排序在前面的，序号都要降低一位。如果在后面的，序号不需要变化
#                 if value_>max:
#                     max=value_

#                 if value_>temp:
#                     self.lru[key_]=value_-1
                
#             self.lru[key]=max
        
#         #不存在
#         else:
#             #当前的长度
#             length=len(self.memory)
#             if length<self.max_size:
#                 #序号从0开始
#                 length+=1
#                 self.memory[key]=value
#                 self.lru[key]=length
#             else:
#                 #越小越寄该删除,在这儿找到需要被替换掉的
#                 min_num=3000
#                 min_key=None
#                 for key_,value_ in self.lru.items():
#                     if value_<min_num:
#                         min_key=key_
#                         min_num=value_
#                     self.lru[key_]=value_-1

#                 del self.memory[min_key]
#                 del self.lru[min_key]

#                 self.memory[key]=value
#                 self.lru[key]=length

#         #         print("此时容量不够，需要删除",min_key,"他这时候调用序号是",min_num,)

#         print(f"######输入了{key, value}########")
#         for key_,value_ in self.memory.items():
#             print(key_,value_,f"{key_,self.lru[key_]}",end=" ")
#         print()
#         print("#############")
#         print()



capacity=3
obj = LRUCache(capacity)
key="1"
value="1"
obj.put(key,value)


key="2"
value="2"
obj.put(key,value)


key="3"
value="3"
obj.put(key,value)

key="4"
value="4"
obj.put(key,value)

print(obj.get("4"))
print(obj.get("3"))
print(obj.get("2"))
print(obj.get("1"))


key="5"
value="5"
obj.put(key,value)

print(obj.get("1"))
print(obj.get("2"))
print(obj.get("3"))
print(obj.get("4"))
print(obj.get("5"))


# print(obj.get("3"))
# print(obj.get("4"))
# key="e"
# value="e"
# obj.put(key,value)

# key="f"
# value="f"
# obj.put(key,value)

