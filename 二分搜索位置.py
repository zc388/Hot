class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1

        #不在二分的过程中，找到 target 就立刻返回
        #
        while(left<=right):
            #先执行普通除法 /，得到浮点数结果，再通过 int() 强制转换为整数（直接截断小数部分）。
            # middle=int((left+right)/2)
            middle=(left+right)//2
            print(middle)
            if nums[middle]<target:
                left=middle+1

            else:
                right=middle-1

            print(left,right)

        #return middle+1，简直是多此一局，因为最后定位时如果没找到，那一定是插在最后一次的俩数字中间！(因为最后一次只有俩)
        return left
        # if target<nums[0]:
        #     return 0
        
        # return middle+1
                
# left=0
# right=len(nums)-1
# while(left<=right):
#     middle=(left+right)//2
#     print(middle)
#     if nums[middle]<target:
#         left=middle+1

#     else:
#         right=middle-1
# return left











nums =[1,3,5]
target = 3
solu=Solution()
print(solu.searchInsert(nums,target))