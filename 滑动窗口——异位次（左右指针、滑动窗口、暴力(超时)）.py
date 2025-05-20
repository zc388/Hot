# for (int l = 0, r = 0 ; r < n ; r++) {
# 	//当前考虑的元素
# 	while (l <= r && check()) {//区间[left,right]不符合题意,在这个题是将不符合的加进去
#         //扩展左边界
#     }
#     //区间[left,right]符合题意，统计相关信息
# }
s = "abab"
p = "ab"
s_len, p_len = len(s), len(p)
if s_len < p_len:
    print()

p_count=[0]*26
for i in range(p_len):
    p_count[ord(p[i])-ord('a')] +=1

ans=[]
l,r=0,0
s_count=[0]*26
for r in range(s_len):
    s_count[ord(s[r])-ord('a')] += 1
    if(r-l+1==p_len):
        if(s_count==p_count):
            ans.append(l)
        s_count[ord(s[l])-ord('a')] -= 1
        l += 1

print(ans)












# s = "cbaebabacd"
# p = "abc"
# s_len, p_len = len(s), len(p)

# #字符串长度小于后面的
# if s_len < p_len:
#     print()

# ans=[]
# s_count = [0] * 26
# p_count = [0] * 26


# #因为每次滑动的窗口大小都和短的那个一样大，所以先初始化一个
# for i in range(p_len):
#     p_count[ord(p[i])-ord('a')] +=1
#     s_count[ord(s[i])-ord('a')] +=1

# if s_count==p_count:
#     ans.append(0)

# #这里应该是s比p长多少，就会有多少（差+1）组出来，所以每次取一定的长度的窗口
    
# #这里滑动窗口大小和p一样大，每次遍历出来的结果其实是滑动窗口中字母出现的次数！因为i会使s_count的第一位和最后一位不断变化，相当于在以一个窗口遍历完s的同时，统计其中字幕出现过的次数
# for i in range(s_len-p_len):
#     #这里是为了维护滑动窗口中出现过的字母的个数

#     #这个代表当前滑动窗口的第一个字母，因为已经初始化过一次，所以进循环的时候可以直接将其减去！
#     s_count[ord(s[i]) - 97] -= 1
#     #中间字母不变
#     s_count[ord(s[i + p_len]) - 97] += 1

#     if(s_count==p_count):
#         ans.append(i+1)
# print(ans)






#暴力解，超时
# p_len=len(p)
# i,j=0,0
# n=len(s)
# count = [0 for x in range(0, 26)]
# ans=[]
# for i,char in enumerate(p):
#     count[ord(char)-ord('a')] +=1

# for i in range(0,n-p_len+1):
#     j=i+p_len-1
#     count1 = [0 for x in range(0, 26)]
#     for k in range(i,j+1):
#         count1[ord(s[k])-ord('a')] +=1
#     if count1 == count:
#         ans.append(i)

# print(ans)

        
