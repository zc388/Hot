matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

bottom, right = len(matrix)-1, len(matrix[0])-1
top,left = 0,0
ans=[]
print(bottom,right)
print(top,left)

while left<right and top<bottom:
    #先从左往右,且天然满足左开右闭
    for i in range(left,right):
        ans.append(matrix[top][i])
    for i in range(top,bottom):
        ans.append(matrix[i][right])
    for i in range(right,left,-1):
        ans.append(matrix[bottom][i])
    for i in range(bottom,top,-1):
        ans.append(matrix[i][left])
    
    right-=1
    bottom-=1
    left+=1
    top+=1

if bottom == top:
    for i in range(left,right+1):
        ans.append(matrix[top][i])
elif left==right:
    for i in range(top,bottom+1):
        ans.append(matrix[i][left])

print(ans)










# visit= visited = [[False] * column for _ in range(row)]
# count=column*row
# ans=[]
# #规定四个方向
# directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# directionIndex = 0
# i=0
# j=0

# for count in range(count):
#     print(i,j,directionIndex)
#     ans.append(matrix[i][j])
#     visited[i][j] = True
#     nextRow,nextColumn= i + directions[directionIndex][0] , j + directions[directionIndex][1]

#     #判断边界，如果不符合这三个条件中任意一个，那就是超界，需要变换换方向
#     if not( 0<=nextRow<row and 0<=nextColumn<column and not visited[nextRow][nextColumn]):
#         directionIndex = (directionIndex + 1) % 4
#     i += directions[directionIndex][0]
#     j += directions[directionIndex][1]

# print(ans)




  