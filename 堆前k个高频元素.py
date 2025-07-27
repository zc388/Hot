#可以用字典，把某个元素的出现次数记录，然后堆记录进行排序，最后返回记录对应的key

# #等通知写法
# from collections import Counter
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """

#         count = Counter(nums)
#         top_k = count.most_common(k)  # 返回前 k 个元素及其次数
#         ans=[]
#         for result in top_k:
#             ans.append(result[0])

#         return ans
#######################################################################################################
#还可以用上一问的快排写法，只要k<目标值即可添加到ans中！



#######################################################################################################
#深入讲解 lambda 函数
#lambda 是 Python 中的匿名函数，用于快速定义简单的函数。它的语法为：        lambda 参数: 返回值
#在这里进行排序，最重要的一点就是items = list(count.items())  # 转换为元组列表：[(key, value), ...]
#将哈希（字典）转化为了元组列表！这样子才可以进行排序（sort实际上就是快排）

#这个比较快，nlogn（基本上就是排序的时间）,再加一个n顶多

# # from collections import defaultdict
# class Solution(object):
#     def topKFrequent(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         if len(nums)==0:
#             return []

#         # count_dict = defaultdict(int)
#         # for num in nums:
#         #     count_dict[num] += 1

#         count_dict={}

#         for num in nums:
#             if num in count_dict:
#                 count_dict[num] += 1
#             else:
#                 count_dict[num] = 1

#         dict_sort=sorted(count_dict.items(),key=lambda x:x[1],reverse=True)
#         # print(dict_sort)
#         ans=[]
#         for i in range(0,k):
#             ans.append(dict_sort[i][0])
#         return(ans)

####################################################################################################################



#还有堆的方法！
#采用最小堆替换法，一直维持一个大小为k的堆，这样子堆顶元素一直就是最小的
#最小堆能保证堆顶元素是堆中最小的。遍历过程中，若当前元素频率大于堆顶，则替换堆顶并调整堆，最终堆中保留的就是最大的 K 个元素。
'''
最小堆的堆顶是堆中最小的元素 → 这是筛选的 “基准线”。
堆大小固定为 K → 确保只保留 “候选的最大 K 个元素”。
新元素频率 > 堆顶频率时才替换 → 用更大的元素替换掉当前最小的候选元素。
遍历结束后，堆中剩下的就是 “所有元素中最大的 K 个” → 因为所有比它们小的元素都被筛选出去了。
'''
#所以初始随意建堆（甚至是空堆），扫过一遍列表就知道哪个是频率最大的了
class Min_Heap():
    def __init__(self,k):
        self.heap=[]
        self.max_size=k
    
    def get_len(self):
        return len(self.heap)

    def _parent(self, idx):
        return (idx - 1) // 2
    
    def _left_child(self, idx):
        return 2 * idx + 1
    
    def _right_child(self, idx):
        return 2 * idx + 2
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def sift_up(self,idx):
        #当父节点，大于当前节点时菜向上挪动，这里我写反了
        while idx>0 and self.heap[self._parent(idx)][1] > self.heap[idx][1]:
            self._swap(idx, self._parent(idx))
            idx = self._parent(idx)
    
    def sift_down(self,idx):
        min_idx=idx
        left=self._left_child(idx)
        min_idx = idx

        left = self._left_child(idx)
        if left < len(self.heap) and self.heap[left][1] < self.heap[min_idx][1]:
            min_idx = left

        right = self._right_child(idx)
        if right < len(self.heap) and self.heap[right][1] < self.heap[min_idx][1]:
            min_idx = right
        
        if idx != min_idx:
            self._swap(idx, min_idx)
            self.sift_down(min_idx)
    
    def push(self, element,freq):
        # 插入元素
        if len(self.heap) < self.max_size:
            # 堆未满时直接插入
            self.heap.append((element,freq))
            self.sift_up(len(self.heap) - 1)

        elif freq > self.heap[0][1]:
            # 堆已满且当前元素频率大于堆顶，替换堆顶
            self.heap[0] = (element,freq)
            self.sift_down(0)  
    
    def peek(self):
        # 查看堆顶元素
        return self.heap[0] if self.heap else None   
        

class Solution(object):
    def topKFrequent(self, nums, k):
        count_dict={}
        for num in nums:
            if num in count_dict:
                count_dict[num]+=1
            else:
                count_dict[num]=1

        print(count_dict.items())


        heap = Min_Heap(k)
        for num, freq in count_dict.items():
            heap.push(num,freq)
            print(heap.heap)



        result = []
        while heap.heap:
            result.append(heap.peek()[0])
            heap.heap[0] = heap.heap[-1]
            heap.heap.pop()
            if heap.heap:
                heap.sift_down(0)
        
        return result



nums = [5,3,1,1,1,3,73,1]
k = 2
solu=Solution()
print(solu.topKFrequent(nums,k))