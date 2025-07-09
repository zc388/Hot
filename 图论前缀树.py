class Node():
    #__slots__ 是一个特殊的类属性，用于显式声明类的实例属性。它通常用于优化内存使用和提高属性访问速度
    #每个 Node 实例的 son 和 end 属性会被存储在一个固定大小的数组中，而不是一个字典中。
    #无法动态添加其他属性。例如，尝试添加 self.extra = 1 会导致 AttributeError
    __slots__ = "son","end"
    
    def __init__(self):
        self.son={}
        self.end=False

#实际上前缀树就是一个二十六杈树
class Trie(object):

    def __init__(self):
        self.root=Node()#初始化根节点

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur=self.root
        for c in word:
            if c not in cur.son:
                cur.son[c]=Node()
                #无论有没有，都更新一下下一层的cur
            cur=cur.son[c]
        cur.end=True#最后一层需要设为end
        return self.root

        #这里写的不对，逻辑全乱了，逻辑应该这样
        #选定初始root，判断是否有子节点，如果son中没有的话，在对应的层数添加一个子节点，往下继续走
        #往下走的过程中，新的root也需要继续更新迭代！
        # for cur in word:
        #     # print(cur)
        #     if cur not in self.root.son:
        #         #如果不在子节点里，那就添加子节点，而不是直接在son里面搞
        #         # self.root.son[int(cur)-int('a')]=cur
        #         self.root.son[cur]=Node()
        #     cur=self.root.son[cur]

    def find(self,word):
        cur=self.root
        for c in word:
            if c not in cur.son:
                #没找到
                return 0
            cur=cur.son[c]
        #找到且终点
        if cur.end==True:
            return 1
        else:
        #找到但不是终点
            return 2
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ans=self.find(word)
        if ans != 1:
            return False
        else: return True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        ans=self.find(prefix)
        if ans ==1 or ans ==2:
            return True
        else: return False
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
node=obj.insert('word')
ans=obj.startsWith('wor')
print(ans)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
        

