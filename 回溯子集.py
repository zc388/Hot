class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(1<<len(nums)):
            #将nums中的数字当成每一位，将八种组合其中的一种拿出来和这仨数字作比较，如果为1就证明选中！
            susbet=[x for j,x in enumerate(nums) if i>>j & 1]
            ans.append(susbet)
        print(ans)

nums = [1,2,3]
solu=Solution()
# solu.subsets(nums)

print(5>>0)