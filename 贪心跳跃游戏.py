#这一个题，感觉要求每一步能到达的最远下一步，其实应该算是动态规划的题

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==0:
            return True
        can_step=0
        for i in range(0,len(nums)):
            if can_step>=i:    
                #我觉得可能存在这种情况
                #2 5 1 1 1 ，从第二个就能直达最后，所以也不用更新
                #2 0 1 1 1 , 这种情况下可以从第一个跳到第二个，但是后面都是1，加上比can_step大，可以更新
                can_step=max(can_step,i+nums[i])
            if can_step>=len(nums)-1:
                return True
        return False











nums = [3,2,1,0,4]
solu=Solution()
print(solu.canJump(nums))