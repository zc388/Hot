from collections import deque

class Solution(object):

    #这个题的难点在于，每一次腐蚀的橘子不一定只有一个，所以需要按照层序来解决，每一次可能有两个或者三个橘子同时污染别的，应该用类似于层序的方法去解决问题
    def orangesRotting(self, grid):
        #假设遍历到一个，就是一分钟，同一分钟可以往四个方向走
        #if 1，遍历四周
        rows=len(grid)
        cols=len(grid[0])
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        fresh=[]
        count=0
        time=0
        queue=deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    fresh.append((row,col))
                if grid[row][col]==2:
                    queue.append((row,col))

        if len(fresh)==0:
            return 0

        while queue:        
            #当前层个数
            rotting=False
            len_q=len(queue)

            #处理
            for _ in range(len_q):
                x,y=queue.popleft()
                for dx,dy in direction:
                    r,c=x+dx,y+dy
                    if 0<=r<rows and 0<=c<cols and grid[r][c]== 1:
                        rotting=True
                        grid[r][c]=2
                        queue.append((r,c))
            if rotting:
                time+=1

        for x,y in fresh:
            if grid[x][y]==1:
                return -1
        return -1 if time ==0 else time
    



grid = [[2,1,1],[1,1,0],[0,1,1]]
solution=Solution()
print(solution.orangesRotting(grid))