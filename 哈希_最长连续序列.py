# 最长连续序列

#给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

nums=[1,0,1,2]
length=0
#这一串可以用一行代码代替
# for i,num in enumerate(nums):
#     hashtable[i]=num
#set在去重的同时会进行排序
num_set=set(nums)
print(num_set)
longest_streak=0

for num in nums:
    #若比当前数小1的不在set中，那么当前的数就需要更新一下，最大连续的数无需更新，但是当前连续数量需要更新
    if num-1 not in num_set:
        current_num = num
        current_streak = 1
        #如果比他大的也在，那就更新最大连续数和当前数，而如果比他大1的数也在的话，下一个自然就是比他大一的
        while current_num+1 in num_set:
            current_num += 1
            current_streak += 1
        
        #比较当前最大和统计的最大连续数字
        longest_streak = max(longest_streak, current_streak)

print(longest_streak)
