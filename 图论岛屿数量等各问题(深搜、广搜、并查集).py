from collections import deque

class Union_Grid:
    def __init__(self,grid):
        self.rows=len(grid)
        self.cols=len(grid[0])
        self.parent=self.cols*self.rows*[-1]
        count=0
        for row in range(self.rows):
            for col in range(self.cols):
                if grid[row][col]=="1":
                    index= row*self.cols + col
                    self.parent[index]=index
                    count += 1
        self.count=count
        self.rank = [0] * self.cols * self.rows 


    def find_root(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find_root(self.parent[x])
        return self.parent[x]
    
    def union_root(self,x,y):
        x_root=self.find_root(x)
        y_root=self.find_root(y)
        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                y_root,x_root=x_root,y_root

            self.parent[y_root]=x_root

            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

            self.count -= 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_count(self):
        print(self.parent)
        return self.count
        
    # #现在这里的写法有错误！当两个点的根节点相同时，不需要再进行合并！！！！
    # #但是我没考虑到
    # def union_root(self,x,y):
    #     x_root=self.find_root(x)
    #     y_root=self.find_root(y)

    #     #这里的逻辑错误了，我们不是根据根节点的大小来进行合并，而是根据秩的大小来进行合并的
    #     # if x_root>y_root:
    #     #     self.parent[y_root]=x_root
    #     # elif x_root<y_root:
    #     #     self.parent[x_root]=y_root
    #     # else:
    #     #     self.parent[x_root]=y_root
    #     #     self.rank[y_root]+=1

    #     #这里我们经过一步处理，反正就是把y并入x中，如果y高于x，那就x，y交换，这样可以少写几行
    #     if self.rank[x_root] < self.rank[y_root]:
    #         y_root,x_root=x_root,y_root

    #     self.parent[y_root]=x_root

    #     if self.rank[x_root] == self.rank[y_root]:
    #         self.rank[x_root] += 1

    #     self.count -= 1



class Solution(object):
    def numIslands(self, grid):
        rows=len(grid)
        cols=len(grid[0])

        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        union=Union_Grid(grid)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    grid[row][col]="0"
                    index=row*cols + col

                    for dx,dy in direction:
                        x , y =row+dx,col+dy
                        if 0 <= x < rows and 0 <= y <cols and grid[x][y]=="1":
                            #这里置0了，其实还需要恢复回去吧，比如当前是测试结果，index旁边的都变成了0，那么它一会儿就被隔离了
                            #这里说的不对哥们！！！并查集的相邻边不需要再进行置0！！！这样可以保证下次扫到他，还可以根据他来判断想邻边
                            # grid[x][y]="0"
                            index_xy=x*cols+y
                            union.union_root(index,index_xy)
                            print(f"现在合并{index,index_xy}")
        ans=union.get_count()
        return ans



#来个神奇的！连通性问题，路径压缩按秩合并
#如果邻边有为1的，那就加入到当前所在的并查集
#这个是标准并查集，现在写个图专用的
# class Union:
#     def __init__(self,n):
#         #初始化时，所有人都是自己的根节点
#         self.parent=list(range(n))
#         #由于并查集是多个集和，所以这里也需要统计高度，用于归类，将矮的并入高的
#         self.rank = [0] * n  # 每个集合的秩（高度）
#         self.count=n

#     def find_root(self,x):
#         #初始时，每个点都是自己，这里返回的也都是自己
#         #后面分类以后，每个点都有父节点，但是只有父节点没有父节点
#         #结合上面两句话，父节点都是parent=自身的结点
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
    
#     def union_root(self,x,y):
#         x_root=self.find_root(x)
#         y_root=self.find_root(y)

#         #存在大小关系时，树的高度不会发生变化，所以秩不用增加
#         if x_root>y_root:
#             self.parent[y_root]=x_root
#         elif x_root<y_root:
#             self.parent[x_root]=y_root
#         else:
#             #相等时，随便一个并入另一个，然后树变高了，秩也要变大
#             self.parent[x_root]=y_root
#             self.rank[y_root]+=1
#         count -= 1

#     def connected(self, x, y):
#         return self.find(x) == self.find(y)
    
#     def get_count(self):
#         return self.count


# class Solution(object):
    
    #并查集,这里的想法很好，但是由于并查集写的没那么好，并查集我用的序号是n，但是在二维矩阵中，序号复杂一些，会越界！所以需要改改喽，完整版的另写！
    # def numIslands(self, grid):
    #     rows=len(grid)
    #     cols=len(grid[0])

    #     nums=rows*cols

    #     #并查集初始化，一共这么多个
    #     #❌！！并查集不是初始化所有的！
    #     #应该仅初始化集合的个数，所以在这儿，只需要初始化值为1的数
    #     union=Union(sum([row.count(1) for row in grid]))

    #     direction = [(0,1),(0,-1),(1,0),(-1,0)]

    #     for row in range(rows):
    #         for col in range(cols):
    #             if grid[row][col] == "1":
    #                 #和前面一样，置0，然后再看他的邻居有没有为1的，如果有，归入并查集，并且置0，再继续别的循环
    #                 grid[row][col]=0
    #                 index = row*cols + col
    #             for dx,dy in direction:
    #                 x,y = row+dx , col+dy
    #                 if 0 <= x < rows and 0 <=y <cols and grid[x][y] == "1":
    #                     grid[x][y] == "0"
    #                     index_tmp= x*cols + y
    #                     union.union_root(index,index_tmp)

    #     ans=union.get_count()
    #     print(ans)



    # 广搜，其实我的想法没问题，就是应该找到所有的1，然后入队❌，不是找到所有的1
    # 但是问题在于如何去判断每次谁该+1，谁该-1
    # 在这里的处理逻辑其实和深搜一样，只要找到了一个1，就将其入队，然后从他开始广搜，把所有的相邻1置零！
    # 也就是说无论怎样都要遍历一遍整个图
    # def numIslands(self, grid):
    #     #行和列数
    #     rows=len(grid)
    #     cols=len(grid[0])
    #     queue=deque()
    #     ans=0
    #     for r in range(rows):
    #         for c in range(cols):
    #             if(grid[r][c]=="1"):
    #                 ans += 1
    #                 #置零
    #                 grid[r][c]="0"
    #                 #append方式不对，因为这里采用append，不需要嵌套！！这里相当于是直接把两个点打包了
    #                 #如果是初始化时，才需要用[], 用于初始化队列的初始元素列表
    #                 queue.append((r,c))
    #                 while queue:
    #                     row,col=queue.popleft()
    #                     for x,y in (row+1,col),(row-1,col),(row,col+1),(row,col-1):
    #                         if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
    #                             queue.append((x,y))
    #                             grid[x][y] = "0"
    #     return ans




    # 这里可以另写一个，也可以直接在循环里写
    # def bfs

    #这是广搜，再来个宽搜
    # def dfs(self,grid,col,row):
    #     box_col=len(grid)
    #     box_row=len(grid[0])
    #     for x,y in (col+1,row),(col-1,row),(col,row+1),(col,row-1):
    #         # print(x,y)
    #         #这里，条件语序判断顺序有问题，应该先判断边界，在判断语句
    #         if 0 <= x < box_col and 0 <= y < box_row and grid[x][y] == "1":
    #             grid[x][y]=0
    #             self.dfs(grid,x,y)
        

    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     ans=0
    #     #使用队列，进行宽搜，搜到一个置0一个.queue不为空，就不停
    #     queue=deque(grid[0][0])
    #     while queue:
    #         print()


    #     # col=len(grid)
    #     # row=len(grid[0])
    #     # # print(col,row)
    #     # ans=0
    #     # for i in range(0,col):
    #     #     for j in range(0,row):
    #     #         if grid[i][j] == "1":
    #     #             ans+=1
    #     #             self.dfs(grid,i,j)

        
    #     print(ans)


grid= [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# union=Union_Grid(grid)
# print(union.parent)
solution=Solution()
print(solution.numIslands(grid))
