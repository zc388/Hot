#Sum of two numbers

#第一题比较简单,直接暴力解也能做（numi+numj=target）

#更快一点的方法就是用字典存储键值对，根据键去找值，键是每一个数，值是序号
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable= dict()
        for i,num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num],i]
            else:
                hashtable[nums[i]]=i
        return []        
        