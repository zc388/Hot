#力扣方法，反过来，遇到不重复的入集合，我的方法是重复的从集合中删掉
'''
我们使用两个指针表示字符串中的某个子串（或窗口）的左右边界，其中左指针代表着上文中「枚举子串的起始位置」，而右指针即为最长不重复子串的结束位置
在每一步的操作中，我们会将左指针向右移动一格，表示 我们开始枚举下一个字符作为起始位置，然后我们可以不断地向右移动右指针，但需要保证这两个指针对应的子串中没有重复的字符。在移动结束后，这个子串就对应着 以左指针开始的，不包含重复字符的最长子串。我们记录下这个子串的长度

'''
s = "bbbbb"
occ = set()
n = len(s)
# 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
rk, ans = -1, 0
for i in range(n):
    if i != 0:
        # 左指针向右移动一格，移除一个字符
        occ.remove(s[i - 1])
    while rk + 1 < n and s[rk + 1] not in occ:
        # 不断地移动右指针
        occ.add(s[rk + 1])
        rk += 1
    # 第 i 到 rk 个字符是一个极长的无重复字符子串
    ans = max(ans, rk - i + 1)

print(ans)




#这个确实要用滑动窗口，有一个简洁模板
'''
//外层循环扩展右边界，内层循环扩展左边界
for (int l = 0, r = 0 ; r < n ; r++) {
	//当前考虑的元素
	while (l <= r && check()) {//区间[left,right]不符合题意,在这个题是将不符合的加进去
        //扩展左边界
    }
    //区间[left,right]符合题意，统计相关信息
}
'''
# s = "bbbbb"
# char_list=set()
# n=len(s)
# max_length=0
# i,j=0,0
# while j<n:
#     char=s[j]
#     tem_max=0
#     #每次遇到不符合的，就删除，并缩减i的长度
#     #其实i在这里仅仅代表，已经经过筛选完成的序列中最大的长度是多少，i到j中的元素是可以有重复的，仅仅是用来计算当前的ij长度差以表示当前的序列长度，其中的内容是会重复，真正的当前不重复序列在set中
#     while(i<=j and (char in char_list) ):
#         char_list.remove(s[i])
#         i +=1
#     char_list.add(char)
#     tem_max=j-i+1
#     max_length=max(tem_max,max_length)
#     j+=1
# print(max_length)











#下面是错误思想，这里考虑的是最长不重复且字母连续子序列，更简单的问题
# s = "pwwkew"
# #ord 字母变数据
# #hrd 数字变字母
# x=ord('a')
# #这里其实使用set更合适，set的查找效率也很高，并且不需要索引，而且没有重复值！！
# count=dict()
# max_lenght=0
# is_Repeated=False
# for i,char in enumerate(s):
#     idx=ord(char)-ord('a')
    
#     if i==0:
#         max_lenght +=1
    
#     else:
#         if is_Repeated:
#             print(idx,char,last_char,ord(char)-ord(last_char),char in count.values())
#             #char in count是错误的，这里我要用的是检查字典中的值，char in count是相当于查索引！！
#             #char in count.values()是一个字符表达式，直接写 == False 会导致逻辑错误
#             if char not in count.values():
#                 is_Repeated=False
#                 max_lenght +=1
#             else: is_Repeated=True
    
    
#     last_char=char
#     count[i]=char
#     print(count)


# print(max_lenght)



# #char in count.values() == False 实际上是一个 链式比较，而不是你期望的逻辑判断。Python 会先计算 char in count.values()，得到一个布尔值，然后再将这个布尔值与 False 进行比较
# #但是用括号包起来就是可以的