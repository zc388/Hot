#灵大佬，用一个数据来存储Tuple，
import math
class MinStack:
    def __init__(self):
        # 这里的 0 写成任意数都可以，反正用不到
        self.st = [(0, math.inf)]  # 栈底哨兵

    def push(self, val: int) -> None:
        self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]


#最小栈，辅助栈
#在每一个元素入栈时，搞一个辅助栈，记录当前的最小元素

# class MinStack(object):

#     def __init__(self):
#         #栈的大小
#         # self.n=n
#         self.stack=[]
#         self.min_stack = [math.inf]

#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.stack.append(val)
#         #比较辅助栈的栈顶，看看当前的最小元素和新入栈的最小是谁
#         self.min_stack.append(min(val,self.min_stack[-1]))
        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         self.stack.pop()
#         self.min_stack.pop()
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.stack[-1]

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         return self.min_stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()