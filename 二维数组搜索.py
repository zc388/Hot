matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
rows, columns = len(matrix),len(matrix[0])
# print(rows,columns)
#快一点的方法，对每行或者每列进行二分

#在Python中，bisect模块提供了一种高效的方法来处理有序序列，允许在不重新排序的情况下进行快速查找和插入操作。
#bisect.bisect_left是该模块中的一个函数，它用于在有序列表中找到一个元素的插入位置，以保持列表的有序性。
is_find=False
for row in matrix:
    l,r=0,len(row)
    while(l<r and is_find==False):
        
        mid=int((l+r)/2)
        print(l,r,mid)
        if row[mid]<target:
            l=mid+1
        elif row[mid]>target:
            r=mid
        else:
            print("找到了")
            is_find=True
            break





#BFS
# visit=[False * columns for _ in range(rows)]

# is_find=False
# row=0
# column=columns-1
# while row<rows and column>=0:
#     if matrix[row][column] >target:
#         column-=1
#     elif matrix[row][column] < target:
#         row+=1
#     else:
#         print("找到了")
#         break


#暴力遍历，我就不写了



        

