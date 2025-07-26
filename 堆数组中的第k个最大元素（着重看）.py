#这里是定义一个大根堆
class MaxHeap:
    def __init__(self):
        self.heap=[]

    def _parent(self,i):
        return (i-1)//2

    def _left_child(self,i):
        return 2*i+1
    
    def _right_child(self,i):
        return 2*i+2

    def _swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def _sift_up(self,i):
        while i > 0 and self.heap[i] > self.heap[self._parent(i)]:
            self._swap(i, self._parent(i))
            i = self._parent(i)
    
    def _sift_down(self,i):
        """下沉元素，维护最大堆性质"""
        max_index = i

        left = self._left_child(i)
        if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
            max_index = left

        right = self._right_child(i)
        if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
            max_index = right

        #如果当前的小于儿子，那就交换
        if i != max_index:
            self._swap(i, max_index)
            self._sift_down(max_index)
    
    def insert(self, value):
        """插入元素到堆"""
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_max(self):
        """提取并返回最大值"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        #自顶向下开始调整
        self._sift_down(0)
        return max_val
    def peek_max(self):
        """返回最大值但不删除"""
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

#双指针快排
class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        return self.quickselect(nums, 0, n - 1, n - k)
    
    def quickselect(self, nums, l, r, k):
        if l == r:
            return nums[k]
        
        #以第一个值作为边界
        partition = nums[l]
        #初始化一下，都放在边界外，因为一会儿要先加一和减一，也可以边界内，处理后再变化值

        #i从前往后找，找比基准大的值
        #j从后往前找，找比基准小的值
        #所以j最后会停留在最后一个比基准小的值的位置，而i不一定停在第一个比基准大的位置
        i, j = l - 1, r + 1
        
        while i < j:
            i += 1
            #从前往后找到第一个大于等于基准的值，这个得放后面
            while nums[i] < partition:
                i += 1
                
            j -= 1
            #从后往前找到第一个小于等于基准的值，这个得放基准前面
            while nums[j] > partition:
                j -= 1
            
            #如果说找到的位置，i在j的前面，那么就说明需要交换了！
            #如果俩相等，那就说明找到的是基准本身了
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        
        #这时候以j为准
        #因为我们是双指针，i和j进行交换划分结束后
        #j的位置是最后一个小于等于基准元素的索引
        if k <= j:
            return self.quickselect(nums, l, j, k)
        else:
            return self.quickselect(nums, j + 1, r, k)



#这里是大佬写法，用小根堆，并且只维护前k个小的值，记得看，现在偷懒了
# class Solution {
#     public int findKthLargest(int[] nums, int k) {
#         for (int i = (k - 1) / 2; i >= 0; i--) {
#             siftDown(nums, i, k);
#         }
#         for (int i = k; i < nums.length; i++) {
#             if (nums[i] > nums[0]) {
#                 nums[0] = nums[i];
#                 siftDown(nums, 0, k);
#             }
#         }
#         return nums[0];
#     }

#     private void siftDown(int[] nums, int curr, int size) {
#         while (curr * 2 + 1 < size) {
#             int next = curr * 2 + 1;
#             if (next != size - 1 && nums[next] > nums[next + 1]) {
#                 next++;
#             }
#             if (nums[curr] > nums[next]) {
#                 swap(nums, curr, next);
#             } else {
#                 break;
#             }
#             curr = next;
#         }
#     }

#     private void swap(int[] nums, int a, int b) {
#         int temp = nums[a];
#         nums[a] = nums[b];
#         nums[b] = temp;
#     }
# }

#这题俩方法，一个是快排，一个是堆排序,
#借鉴于快排，来一个快速选择
#每次将序列划分为两部分，大于pivvt的放一半，其他的放另一个半

#哎呦我操，超出时间限制了，因为盲目选最后一个，极端条件下时间复杂度贼大，所以可以采用三数取中法
#这个是单向循环遍历，在一定情况下时间复杂度会很高，比如有顺序的数组，可以看一下，双指针遍历快排搜索
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         def quicksort(l,r,k):
#             if l==r:
#                 return nums[l]
            
#             #快排反正本来就要随机选一个数当做标杆，那就随机选最小或最大的那个,这里很明显，我选了最大值
            
#             pivot_cur=nums[r]
#             #store_index理解为，小于或者大于k的数组的最后一个位置
#             store_index=l

#             for i in range(l,r):
#                 #真笨啊，直接选最后一个，大于他的直接交换位置了，小于的话其实不用动的，因为小的本来就在标杆的右面
#                 #原来写的坐标位置是cur，那为什么是和store_index换？
#                 if nums[i]>=pivot_cur:
#                     nums[i],nums[store_index ]=nums[store_index],nums[i]
#                     #这里需要多一个记录，记录一下当前的起点到交换点，走过了几步
#                     store_index+=1
            
#             #所以这个store记录的其实就是，pivot最终应该在的位置
#             nums[store_index], nums[r] = nums[r], nums[store_index]
#             #更新基准的位置
#             new_pivot_index = store_index
            
#             #计算一下当前的位置，距离当前的起始是否满足k个距离。
#             # 为啥要加1？
#             # 因为我们l从0开始的,天生少了一个
#             count=new_pivot_index-l+1
#             print(pivot_cur,new_pivot_index,k,nums)
#             if count==k:
#                 return nums[new_pivot_index]
#             #也就是说不满足，那就在当前基准的右半边
#             elif count<k:
#                 return quicksort(new_pivot_index+1 , r, k-count)
#             #也就是说在左半边，那就是说基准大大的满足，但是满足过头了，需要往回缩
#             elif count>k:
#                 return quicksort(l,new_pivot_index-1,k)
        
#         ans=quicksort(0,len(nums)-1,k)
#         return ans




#主打的是
#最大最小堆，这里是算法的写法
#每次和父节点比较即可
#比到n\2即可
#从后往前调整，将父节点和子结点中大的那个交换（大根堆）

# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         n=len(nums)

#         def heapify(i,size):
#             largest=i
#             left=2*i+1
#             right=2*i+2
#             if left<size and nums[left]>nums[largest]:
#                 largest=left
#             #这里一开始我还在怀疑，如果两个人都更新了largest，会不会冲突
#             #答案是不会，因为上面即便更新了，下面取得也是当前最大值的坐标，而不是i的坐标，所以会选最大的largest
#             if right<size and nums[right]>nums[largest]:
#                 largest=right
#             if largest!=i:
#                 nums[largest],nums[i]=nums[i],nums[largest]
#                 #再从当前的排序好的这个坐标点往上排
#                 heapify(largest,size)
        
#         #构建一个初始的堆
#         #一开始写的0，n,这是错的！因为需要从后往前找，也就是从n/2开始！
#         # for i in range(0,n):
#         for i in range(n//2-1,-1,-1):
#             heapify(i,n)

#         #建堆之后，不断地取出，然后从上往下调整堆的顺序
#         #由于已经建堆，所以调整时只需要从上往下即可
#         for _ in range(k-1):
#             #交换顶和位
#             nums[0], nums[n-1] = nums[n-1], nums[0]
#             #总数再减一
#             n -= 1
#             heapify(0,n)
#         return nums[0]


nums=[3,2,3,1,2,4,5,5,6]
print(nums)
k = 4
solu=Solution()
print(solu.findKthLargest(nums,k))