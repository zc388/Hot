class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 双重循环（冒泡思想），错误，无法处理连续0的情况
        # for i,num in enumerate(nums):
        #     if nums[i] == 0 :
        #         for j in range(i,len(nums)-1):
        #             if j < len(nums)-1:
        #                 tem=nums[j]
        #                 nums[j]=nums[j+1]
        #                 nums[j+1]=tem
        # return nums

        #统计的方法试一下，但是需要三个循环
        count=0
        for i,num in enumerate(nums):
            if num != 0:
                count +=1

        j=0
        for i,num in enumerate(nums):
            if num!=0:
                nums[j]=num
                j += 1

        for i in range(count,len(nums)):
            nums[i]=0
        return nums

        #官方题解，双指针，交换左指针扫到的0和右指针待处理序列的非零数
        n=len(nums)
        left=0
        right=0
        #快慢指针，左指针指向处理好的最后一个，右指针指向待处理的第一个
        #左快右慢
        while right<n:
            #只要右指针扫到了第一个非0数，交换左右指针，处理好的序列+1
            if nums[right]!=0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            right += 1
        return nums


