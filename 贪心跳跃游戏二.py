#这一个题，感觉和上一个差不多啊，就加个计数？



'''
在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。
如果访问最后一个元素，在边界正好为最后一个位置的情况下，我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。

'''
class Solution:
    def jump(self, nums):
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step



#贪心的想法是每一步选到最大，当前的最优解
# 直到到达了自己的最大值地点时才进行跳步，同时也可以选出当前的最大可到达地点，时max还是num[i]+i
# 由于题目说了是可到达，所以也不用判断是否真的能到达，只需要计算跳步过程就行，max_step也一定会大于len(nums)


#我的解法是，只要遇见比自己大的就+1，就算最后的结果一样，但是会有许多多余的步骤


#方法差不多，但是对于计数的部分写的不对，官解如上
# class Solution(object):
#     def jump(self, nums):
#         if len(nums)==1:
#             return 0

#         can_step=0
#         count=0
#         for i in range(0,len(nums)):
#             if can_step>=i:
#                 tem=i+nums[i]
#                 if tem>can_step:
#                     count+=1
#                     can_step=tem

#             if can_step>=len(nums)-1:
#                 break
                
#         return count

nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
solu=Solution()
print(solu.jump(nums))