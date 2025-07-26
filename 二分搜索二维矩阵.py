#两次二分啊哥们
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col=len(matrix)-1
        row=len(matrix[0])
        up=0
        down=len(matrix)-1
        while up<=down:
            mid=(up+down)//2
            if matrix[mid][row-1] < target:
                up=mid+1
            else:
                down=mid-1

        print(up)

        if up >col:
            return False
        
        left=0
        right=len(matrix[0])-1
        mat=matrix[up]

        while left<=right:
            mid=(left+right)//2
            if mat[mid]<target:
                left=mid+1
            elif mat[mid]>target:
                right=mid-1
            else:
                return True
                
        return False

#普通解法
# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         col=len(matrix)-1
#         row=len(matrix[0])
#         up=0
#         down=len(matrix)-1
#         while up<=down:
#             mid=(up+down)//2
#             if matrix[mid][row-1] < target:
#                 up=mid+1
#             else:
#                 down=mid-1

#         print(up)

#         if up >col:
#             return False
        
#         for i in matrix[up]:
#             print(i)
#             if i==target:
#                 return True
                
#         return False




matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solu=Solution()
print(solu.searchMatrix(matrix,target))