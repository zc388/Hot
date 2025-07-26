#题解的思路，每次在合适的时候判断好区间，也可以做这个题
#在判断完中间之后再根据num[0]来判断即可，因为如果反转，那么nums[0]一定是大区间，另一个就是小区间，
#先对nums[0]和nums[mid]进行判断，如果nums[0]<numd[mid]，那么mid一定是在反转点的后面
#反之，mid在翻转点前，这两种情况对应的r和left不同

#以nums[0]<num[mid]举例，即翻转点在mid后面
#所以如果nums[0]<targer<nums[mid]，那肯定在翻转后的地方，【0，mid】这部分，但是要注意，mid的位置不是翻转发生位置！
#   如果nums[0]大于target,或者targer>nums[mid]，那肯定在未翻转的地方，【mid，0】这一部分

#反过来就要和数组的最后一个元素进行对比了
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if not nums:
#             return -1
#         l, r = 0, len(nums) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[0] <= nums[mid]:
#                 if nums[0] <= target < nums[mid]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#             else:
#                 if nums[mid] < target <= nums[len(nums) - 1]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#         return -1



#我的想法，先给他数组纠正，再二分，或者找到旋转点，两次二分
#想法很对，但错误也会出现，全是等于号时的判定不正确！
class Solution(object): 
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cur=0
        for i in range(0,len(nums)):
            if i+1<=len(nums)-1 and nums[i]>nums[i+1]:
                cur=i
                break


        left=self.search_mid(nums[0:cur+1],target)
        if nums[left]==target:
            return left

        print(cur,"#############")
        left=cur+self.search_mid(nums[cur+1:],target)+1

        print(left)
        if left<=len(nums)-1 and nums[left]==target:
            return left

        return -1

    def search_mid(self,nums,target):
        if not nums:
            return 0
        
        left=0
        right=len(nums)-1
        while(left<=right):
            middle=(left+right)//2
            if nums[middle]<target:
                left=middle+1

            else:
                right=middle-1

        # print(left,len(nums))
        if left>len(nums)-1 or nums[left]!=target:
            left=0
        return left


nums = [3,5,1]

target = 1
solu=Solution()
print(solu.search(nums,target))