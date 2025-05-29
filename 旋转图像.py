matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)
for i in range(n // 2):
    for j in range((n + 1) // 2):
        #python可以无痛交换，不需要temp代替了
        matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
            = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
print(matrix)
#题目不允许使用辅助数组
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rows, columns = len(matrix), len(matrix[0])

# matrix_copy=[[0] * columns for _ in range(rows)] 

# for row in range(rows):
#     for column in range(columns):
#         matrix_copy[column][rows-row-1]=matrix[row][column]

# print(matrix_copy)