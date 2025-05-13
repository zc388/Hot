nums=[1,8,6,2,5,4,8,3,7]
max_volume=0
left=0
right=len(nums)-1

#错误，同时移动左右指针会造成情况的丢失，只能实现两边对称的取桩子，无法取到不对称，但是容量最大的情况，正确的情况应该是比较左右谁大，然后将小的那个进行替换，类似于贪心
# while right != left:
#     Volume=(right-left)*min(nums[right],nums[left])
#     print(right,left,nums[left],nums[right],right-left,min(nums[right],nums[left]),Volume)
#     if Volume>max_volume:
#         max_volume=Volume
#         # print(max_volume,left,right)
#     right -= 1
#     left +=1
#     print("#########")
#正确的解法
#因为短的不动，不可能比之前上一次更多。
while right > left:
    Volume=(right-left)*min(nums[right],nums[left])
    # print(right,left,nums[left],nums[right],right-left,min(nums[right],nums[left]),Volume)
    if Volume>max_volume:
        max_volume=Volume
        # print(max_volume,left,right)
    if nums[right]>nums[left]:
        left +=1
    else:
        right -= 1
    print("#########")

print(max_volume)