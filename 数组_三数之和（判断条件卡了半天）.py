

nums = [1,-1,-1,0]
nums = sorted(nums)
ans=[]
num_len=len(nums)

for i in range(0,num_len):
    if i>0 and nums[i]==nums[i-1]:
        continue

    k=num_len-1

    for j in range(i+1,num_len):
        print(f"i={i} num[{i}]={nums[i]},j={j} num[{j}]={nums[j]},k={k} num[{k}]={nums[k]}")
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        
        # print(f"i={i},j={j},k={k}")
        #问题出在这（nums[j]+nums[k]+nums[i] ！= 0），这里的三者相加初始值！=0的话，分为两种情况，
        #一种的合>0,另一种是合<0，
        #如果小于0，没有继续的必要，当前的j对应的k一定是目前最大的值，如果这都小于0，那必须要增大j对应的数，只能j++。所以可以直接break（可以在代码中加入判断，目前没加），那么k就算再往里取，那么也会一直小于0，这样做k会不断的减小，在第一轮直接减为1，并在当前i的循环中，不论j为几，k均为1.所以直接跳过了所有的while，并且还有可能出现j>k的情况，所以错误！！
        
        #如果大于0，就说明当前情况下的加和大于零，当k变小，即取到的值num[k]减小时，是有一定几率取到0的。如果当前的while结束了只有两种可能
        #加和<=0,当前组合最接近0的正数或0本身，或复数
        #k<=j了，这种情况下进行相等判断，如果不相等，那就是小于0，也就是说没有符合条件的情况，要么是小于0，要么是大于0

        #在大于0的情况中，我还在考虑会不会出现漏掉情况（比如相加小于0，所以要提j，但是k一直在减小，所以会忽略掉更大的num[j]和小一点的num[k]），但是经过举例子，我发现不会出现这种情况,因为加和小于0的情况已经被筛选了




        """
        所以有两种方法
        要么条件是  （加和！=）且加和<0时continue
        要么条件就直接时大于等于0
        """
        while k>j and nums[j]+nums[k]+nums[i] > 0:
            # print(f"while中，i={i},j={j},k={k}")
            # print(nums[i],nums[j],nums[k])
            k=k-1

        #这里忘记了k和j的筛选，条件判断
        # if k==j:break

        if nums[i]+nums[j]+nums[k]==0:
            ans.append([nums[i],nums[j],nums[k]])
                
print(ans)
# for i in range(0,num_len):
#     if i==0 or nums[i]!=nums[i-1]:

#         k=num_len-1

#         for j in range(i+1,num_len):

#             if j==i+1 or nums[j]!=nums[j-1]:

#                 while k>j and nums[i]+nums[j]+nums[k]!=0:
#                     k=k-1

#                 #这里忘记了k和j的筛选，条件判断
#                 if k==j:
#                     break

#                 if nums[i]+nums[j]+nums[k]==0:
#                     ans.append([nums[i],nums[j],nums[k]])
                
                







# def compared(nums1,nums2):
    
#     length=len(nums1)
#     nums1=sorted(nums1)
#     nums2=sorted(nums2)
#     for i in range(0,length):
#         if nums1[i]!=nums2[i]:
#             return False
    
#     return True


# nums = [-4,-8,7,13,10,1,-14,-13,0,8,6,-13,-5,-4,-12,2,-11,7,-5,0,-9,-14,-8,-9,2,-7,-13,-3,13,9,-14,-6,8,1,14,-5,-13,8,-10,-5,1,11,-11,3,14,-8,-10,-12,6,-8,-5,13,-15,2,11,-5,10,6,-1,1,0,0,2,-7,8,-6,3,3,-13,8,5,-5,-3,9,5,-4,-14,11,-8,7,10,-6,-3,11,12,-14,-9,-1,7,5,-15,14,12,-5,-8,-2,4,2,-14,-2,-12,6,8,0,0,-2,3,-7,-14,2,7,12,12,12,0,9,13,-2,-15,-3,10,-14,-4,7,-12,3,-10]
# ans=[]
# num_len=len(nums)
# for i in range(0,num_len):
#     for j in range(i+1,num_len):
#         for k in range(j+1,num_len):
#             a=[nums[i],nums[j],nums[k]]
#             if nums[i]+nums[j]+nums[k] == 0:
#                 ans.append(a)
# for i in range(len(ans) - 1, -1, -1): 
#     for j in range(len(ans) - 1, i, -1):  
#         if compared(ans[i], ans[j]):
#             del ans[j]
#         if len(ans) < 2:
#             break

# unique_ans = []
# for item in ans:
#     if not any(compared(item, existing) for existing in unique_ans):
#         unique_ans.append(item)

# #python的循环会强制按照第一次循环时的len(ans)，即便后面的ans长度发生变化，也不会修改循环次数！所以可能需要倒序排序、布尔标记、或者列表推导
# # for i in range(0,len(ans)):
# #     print("i",i)
# #     for j in range(i+1,len(ans)):
# #         print(j)
# #         if compared(ans[i],ans[j]):
# #             del ans[j]
# #         print("len",len(ans))

# #         if len(ans)<2:
# #             print("xiaoyu2")
# #             break
        
# #     print("+++++++")
# for i in range(len(ans) - 1, -1, -1): 
#     for j in range(len(ans) - 1, i, -1):  
#         if compared(ans[i], ans[j]):
#             del ans[j]
#         if len(ans) < 2:
#             break


# print(ans)




# '''
# my_list = [1, 2, 3, 4, 3, 5]
# my_list.remove(3)  # 删除第一个值为 3 的元素
# print(my_list)  # 输出：[1, 2, 4, 3, 5]



# my_list = [1, 2, 3, 4, 5]
# del my_list[2]  # 删除索引为 2 的元素
# print(my_list)  # 输出：[1, 2, 4, 5]

# my_list = [1, 2, 3, 4, 5]
# del my_list[1:3]  # 删除索引从 1 到 3（不包括 3）的元素
# print(my_list)  # 输出：[1, 4, 5]

# my_list = [1, 2, 3, 4, 5]
# del my_list  # 删除整个列表
# # print(my_list)  # 报错：NameError，因为 my_list 已被删除



# 删除指定索引的元素
# my_list = [1, 2, 3, 4, 5]
# removed_element = my_list.pop(2)  # 删除索引为 2 的元素，并返回该元素
# print(my_list)  # 输出：[1, 2, 4, 5]
# print(removed_element)  # 输出：3
# 删除最后一个元素
# my_list = [1, 2, 3, 4, 5]
# removed_element = my_list.pop()  # 删除并返回最后一个元素
# print(my_list)  # 输出：[1, 2, 3, 4]
# print(removed_element)  # 输出：5



# 使用列表推导式
# my_list = [1, 2, 3, 4, 5, 6]
# # 删除所有偶数
# my_list = [x for x in my_list if x % 2 != 0]
# print(my_list)  # 输出：[1, 3, 5]



# 使用 filter() 函
# my_list = [1, 2, 3, 4, 5, 6]
# # 删除所有偶数
# filtered_list = list(filter(lambda x: x % 2 != 0, my_list))
# print(filtered_list)  # 输出：[1, 3, 5]




# 删除所有元素
# my_list = [1, 2, 3, 4, 5]
# my_list.clear()  # 清空列表
# print(my_list)  # 输出：[]




# 使用集合去重（不保持顺序）
# my_list = [1, 2, 2, 3, 4, 4, 5]
# my_list = list(set(my_list))
# print(my_list)  # 输出：[1, 2, 3, 4, 5]（顺序可能不同）

# 使用字典保持顺序
# my_list = [1, 2, 2, 3, 4, 4, 5]
# my_list = list(dict.fromkeys(my_list))
# print(my_list)  # 输出：[1, 2, 3, 4, 5]
# '''
