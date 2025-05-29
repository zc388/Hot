matrix=[[1,1,1],[1,0,1],[1,1,1]]
#比较好的思路，直接将需要置0的数组所在的行和列进行统计即可




#搞了一个标记数组，标记等于0的位置，然后再单独处理所需的位置
# columns=len(matrix)
# Rows=len(matrix[0])
# # print(columns,Rows)
# zero=[]
# # print(len(matrix[1]))
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j]==0:
#             zero.append([i,j])

# # for row in matrix:
# #     print(row)

# for z in zero:
#     x=z[0]
#     y=z[1]
#     for c in range(0,columns):
#         matrix[c][y]=0
#     for r in range(0,Rows):
#         matrix[x][r]=0


# # for row in matrix:
# #     print(row)
# # print(zero)

        