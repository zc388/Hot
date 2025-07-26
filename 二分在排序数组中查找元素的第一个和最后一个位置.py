#所以可以将等于和大于合并，这样的话right就会一直减小,或者left一直增大，即便是已经找到了target的位置，left还是会朝着最后一次位置变化，最终停留在第一个left的位置！
class Solution(object):    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            print(mid)
            if nums[mid] >= target:
                right = mid - 1 

            else:
                left = mid + 1
        
        return left
    def searchRange(self, nums, target):
        start = self.searchInsert(nums, target)
        if start==len(nums) or nums[start]!=target:
            return[-1,-1]
        end=self.searchInsert(nums,target+1)-1

        return[start,end]









#这个方法是错误的，因为按照这种写法，当mid正好等于其所在位置时，不再进行二分，直接退出，答案也永远只有一个位置
# class Solution(object):
#     def searchRange(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         if not nums:
#             return [-1,-1]
        
#         ans=[]
#         left=0
#         right=len(nums)-1

#         while left<=right:
#             mid=(left+right)//2
#             if nums[mid]<target:
#                 left=mid+1
#             elif nums[mid]>target:
#                 right=mid-1
#             else:
#                 ans.append(left)
                

#         if nums[left]!=target:
#             return [-1,-1]
        
#         return [ans[0],ans[-1]]










nums = [5,7,7,8,8,10]
target = 8
solu=Solution()
print(solu.searchRange(nums,target))