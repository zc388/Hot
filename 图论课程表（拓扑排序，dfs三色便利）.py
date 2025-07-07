from collections import deque


'''
解法二

拓扑排序
第一轮先将所有没有前置结点的结点入队
每一次都从队列中出队列一个元素，将其子结点全部入队。
循环往复，如果有环，这个循环就不可能结束。
but，怎么进行判断？难道也是设立visit数组？

拓扑排序的顶点数等于图的总顶点数，则图是无环的；否则，图中存在环。


好吧，上面只是个人分析，真正的在下面
拓扑排序（Kahn 算法）
拓扑排序是对有向无环图的顶点进行排序的算法，使得对于每一条有向边 (u, v)，顶点 u 在排序中都出现在 v 之前。如果图中存在环，则无法完成拓扑排序。
核心思想
入度（In-degree）：顶点的入度是指指向该顶点的边的数量。
算法流程：
计算每个顶点的入度。
将所有入度为 0 的顶点加入队列（或栈）。
从队列中取出一个顶点，将其加入拓扑排序结果中，并删除从该顶点出发的所有边（即减少其邻接顶点的入度）。
重复步骤 上一步，直到队列为空。



若拓扑排序的顶点数等于图的总顶点数，则图是无环的；否则，图中存在环。
'''

#计算每个点的入度，计算总共的入度
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        #邻接表中每一个元素是列表
        adj= [ [] for _ in range(numCourses)]
        in_degree=[0]*numCourses
        for v,u in prerequisites:
            adj[u].append(v)    # u -> v
            in_degree[v]+=1
        
        queue=deque([node for node in range(numCourses) if in_degree[node]==0])
        count=0

        while queue:
            node=queue.popleft()
            count+=1
            #❌想法
            # #u能到v，adj中添加的是u能到达的地方，所以直接查询邻接表的node，就知道node所在的索引，也就是谁能到node，但是在这儿不合适，因为我们是要找node能到谁，所以直接用node的邻接表
            # queue.append(adj.index(node))
            #
            for v in adj[node]:
                #被访问的点入度减一
                in_degree[v]-=1
                if in_degree[v] == 0:
                    queue.append(v)
        
        return count==numCourses
        
        


# '''
# 解法一，dfs三色环

# 由于代码没有办法直观的给出每个结点的访问状态，也就是无法直接的判断是否存在环
# 但是深搜是一个栈入栈出的过程，如果一个点进去又出来，就会存在重复递归
# 我们可以通过标记某个结点是否正在递归，来判断他是否完成了访问

# 因为栈是一次递归，访问完就释放出去了，所以一般情况下是只有访问和访问完成两个状态
# '''
# class Solution(object):
#     #dfs,标记状态，如果0代表不连通，1代表连通，-1代表已经访问过，不允许访问

#     #题目给定了prerequisites只有俩元素，这题没有我想象中的那么复杂的情况
#     #由于不重复，并且只有俩，所以可以用一维数组直接指定

#     #0代表未访问，1代表正在访问，2代表访问完了
#     def canFinish(self, numCourses, prerequisites):
#         #构建邻接表
        
#         adj= [ [] for _ in range(numCourses)]
#         for v,u in prerequisites:
#             adj[u].append(v)

#         print(adj)

#         visit=[0]*numCourses
#         #node代表当前课程需要访问的点
#         def dfs(node):
#             if visit[node]==1:
#                 return False
            
#             if visit[node]==2:
#                 return True
            
#             visit[node]=1
            
#             # dfs(adj[node])
#             for v in adj[node]:
#                 if not dfs(v):
#                     return False

#             visit[node]=2

#             return True
            
        
#         #这里需要对每一个点都进行判断！
#         for u in range(numCourses):
#             if visit[u] == 0:
#                 if not dfs(u):
#                     return False
                


#         return True



#检查DAG（有向无环图有两种方式，一个是dfs，另一个是拓扑排序）
#在仅仅进行检测时，使用dfs，在需要排序时，可以使用另一个

#拓扑排序：通过入度数组和队列实现，适合判断是否能完成所有任务（如课程表问题），并可同时生成可行的任务顺序。
#DFS：通过三色标记法检测后向边，实现更简洁，适合单纯判断图是否为 DAG。

# class Solution(object):
#     #dfs,标记状态，如果0代表不连通，1代表连通，-1代表已经访问过，不允许访问
#     def canFinish(self, numCourses, prerequisites):
#         if not prerequisites:
#             return True
        
#         grid = [[0] * numCourses for _ in range(numCourses)]
        
#         for row in grid:
#             print(row)

#         for connect in prerequisites:
#             index = len(connect) - 1
#             end = connect[index]
#             for i in range(0, index):
#                 start = connect[i]
#                 grid[start][end] = 1 

#         for row in grid:
#             print(row)


    #这个题我感觉，就是互相判断前缀即可,如果存在两门课程互为前缀，那就不能完成

    #进一步分析，这应该抽象有向无环图，也就是判断这个题是否为一个有向无环图，如果不是，则不能完成！

    #所以任务转变为，分析这个图中是否有环
    #所以相当于建立一个邻接矩阵
    '''
    现在的写法共享引用问题！！！修改时会全部修改！谨记！
    numCourses * [row] 创建的是 numCourses 个对 同一个列表对象 的引用，而不是 numCourses 个独立的列表。
    因此，当你修改 grid[0][0] 时，由于 grid[0] 和 grid[1] 指向同一个列表，grid[1][0] 也会被修改。
    示例说明：
    初始时 grid 看起来是 [[0, 0], [0, 0]]，但实际上是 [row, row]（两个引用指向同一个 row）。
    当执行 grid[0][0] = 1 时，相当于 row[0] = 1，因此 grid[1][0] 也变成了 1。 
    '''
    # def canFinish(self, numCourses,prerequisites):
    #     if not prerequisites:
    #         return True
        
    #     #先构图
    #     row=[0]*numCourses
    #     grid=numCourses*[row]
    #     for row in range(len(grid)):
    #         print(grid[row])

    #     for connect in prerequisites:
    #         index=len(connect)-1
    #         end=connect[index]
    #         for i in range(0,index):
    #             start=connect[i]
    #             print(start,end)
    #             grid[start][end]=1

    #     print()
    #     for row in range(len(grid)):
    #         print(grid[row])


solution=Solution()
numCourses = 2
prerequisites = [[1,0]]
print(solution.canFinish(numCourses,prerequisites))