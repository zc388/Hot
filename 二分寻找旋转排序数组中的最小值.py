#On的方法，直接遍历一遍
#二分找临界？
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid

        return nums[left]



#贪心写法
#就是说，每一次的mid，一定有一边是有序，另一边是无序
#并没每一次都能判断出哪一边是升序的
#所以，直接在有序的那边选择最小的，将其于上一个最小值进行对比
# class Solution(object):
#     def findMin(self,nums):
#         left=0
#         right=len(nums)-1
#         ans=10000

#         while(left<=right):
#             mid=left+(right-left)//2
#             if(nums[0] <= nums[mid]):
#                 ans = min(ans, nums[0])
#                 #有序区的最小值已经选出来，收缩左边界
#                 left = mid + 1
#             else:
#                 #因为nums[0]>nums[mid]，那么mid肯定是当前最小的
#                 ans=min(ans,nums[mid])
#                 #有序区最小值选出来了，收缩右边界
#                 right=mid-1

#         return ans











nums =[3,4,5,1,2]

solu=Solution()
print(solu.findMin(nums))