#力扣，单调栈
#单调栈压栈和弹栈时需要维护单调性，而且存的是索引，我存的是元素
height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans=0
stack=[]
i=0
while i <len(height):
    #栈不为空，并且当前的值大于栈顶元素，进行判断，当前的雨水量
    while stack and height[i]>height[stack[-1]]:
        top=stack.pop()
        print(top)
        #要是栈为空，没必要再判断，数据不够
        if not stack:
            break
        #取原top的左边的元素，但是不出栈
        left=stack[-1]
        width=i-left-1
        print("#",top,left,width)
        #判断一下是左边的高，还是新的这个i更高，选低的那一个，不断地重复while，直到当前的i不再大于栈中的元素
        height_=min(height[i],height[left]) - height[top]
        ans+=width*height_
    stack.append(i)
    i=i+1

print(ans)
    




#能解，时间超过限制，O(n²)，看了一下单调栈的概念，感觉是我的方法进阶，我是遇到比自己大的，直接停止当下的循环，进行到目前为止的判断，最快的情况下是O(n),最慢是O(n²)
# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         ans=0
#         stack=[]
#         i=0
#         #这里犯了一个大问题，python没有java那么智能，迭代过程中修改变量i，并不会影响迭代过程
#         while i < len(height):
#             if(height[i]>0):
#                 j=i
#                 #此时出栈，要么就是快指针所指的值大于了慢指针i，要么就是快指针超界，没有比当前i更大的了
#                 while height[i]>=height[j] and j<len(height):
#                     stack.append(height[j])
#                     if j<len(height)-1:
#                         j+=1
#                     else:
#                         break
                
#                 #如果是因为到头了终止循环，那么当前的height[i]是最高的,同时，栈也需要清空！，时候不用管i，i+1即可
#                 if j>len(height)-1:
#                     #直接赋空值，或者就是直接clear
#                     print("j超界")
#                     stack=[]
#                     continue
#                 #没到头，说明有一个比他高的，所以前面的全部出栈
#                 else:
#                     #这一部分逻辑是没有问题，但是i=j后，j不停止，不知道为啥
#                     for k in range(0,len(stack)):
#                         top=stack.pop()
#                         if not stack:
#                             break
#                         tem_ans=height[i]-top
#                         ans += tem_ans
#                     i=j
                
#                 i=i+1




################################################################################################################
#感觉没啥问题，但是只能过一个样例，无奈，看看题解吧
#也就是说我的方法只适用于height=[0,1,0,2,1,0,1,3,2,1,2,1]的情况？
  
#我现在的方法，一层循环选起点，循环内使用双指针不断地移动终点
#每次循环算出当前起点和终点的位置，存入栈，栈内即为本次可存水的最大范围
# height = [4,2,0,3,2,5]
# ans=0
# stack=[]
# #这里犯了一个大问题，python没有java那么智能，迭代过程中修改变量i，并不会影响迭代过程
# for i in range(0,len(height)):
#     if(height[i]>0):
        
#         j=i
#         print(f"##############第{i}轮，j从{j}开始################")

#         #此时出栈，要么就是快指针所指的值大于了慢指针i，要么就是快指针超界，没有比当前i更大的了
#         while height[i]>=height[j] and j<len(height):
            
#             stack.append(height[j])
#             print(f"i={i},j={j},stack={stack}")
#             if j<len(height)-1:#len(height)=12
#                 j+=1
#             else:
#                 break
        
#         #如果是因为到头了终止循环，那么当前的height[i]是最高的,同时，栈也需要清空！，时候不用管i，i+1即可
#         if j>len(height)-1:
#             #直接赋空值，或者就是直接clear
#             print("j超界")
#             stack=[]
#             continue
#         #没到头，说明有一个比他高的，所以前面的全部出栈
#         else:
#             print("====")
#             #这一部分逻辑是没有问题，但是i=j后，j不停止，不知道为啥
#             for k in range(0,len(stack)):
#                 top=stack.pop()
#                 if not stack:
#                     break
#                 tem_ans=height[i]-top
#                 ans += tem_ans
#             print(f"ans={ans},i={i},j={j},stack={stack}")
#             i=j
            

# print(ans)

#######################################################################################################################
#单纯用数组去记录求解的方法没问题，但问题是如果遇到一根柱子，如果后面的柱子一直没有超过他，那么从他开始记录的存水量就是错的
#使用动态规划或者单调栈，当遇到比他高的时，再将之前的柱子出栈
#正好看一下栈
'''
用列表实现栈
stack = []
stack.append(element)
element = stack.pop()//前提是栈不为空，栈如果为空需要进行判断
top_element = stack[-1]//取栈顶，前提是栈不为空，栈如果为空需要进行判断

if not stack:
    print("栈为空")
else:
    print("栈不为空")

size = len(stack)

用collections.deque实现
from collections import deque

stack = deque()

# 压栈
stack.append(1)
stack.append(2)
stack.append(3)

# 弹栈
element = stack.pop()
print(element)  # 输出：3
print(stack)    # 输出：deque([1, 2])
'''
# for i in range(0,len(height)):
#     if(height[i]>0):
#         j=i
#         last_ans=0
#         while height[i]>=height[j] and j<len(height)-1:
#             tem_ans=(height[i]-height[j])
#             ans += tem_ans
#             # last_ans +=(height[i]-height[j])
#             print(f"i={i},j={j},height[{i}]={height[i]},height[{j}]={height[j]},last_tem={last_ans},当前tem_ans={(height[i]-height[j])*(j-i)},ans={ans}")
#             j+=1

          #这里不能盲目的i=j，只有进行计算存水量之后再i=i，进行替换，因为可能有根棍子很长，后面的都不能构成水池，但是这样子j就到了最后，那i也就提前终止了
#         i=j

