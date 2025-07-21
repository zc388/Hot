#补充灵神的优化
from collections import Counter
#用于高效地统计可哈希对象的出现次数
'''
all_chars = []
for row in board:      # 遍历每一行
    for c in row:      # 遍历当前行的每个字符
        all_chars.append(c)
和
cnt = Counter(c for row in board for c in row)

等价
'''
class Solution:
    def exist(self, board, word: str) -> bool:
        cnt = Counter(c for row in board for c in row)#这里记录在board中，每个字母的字数

        #这里相当于，先对比一下，word中所有字母出现次数和cnt(即board中字母出现次数)的大小关系
        if not cnt >= Counter(word):  # 优化一
            return False
        
        #从出现次数少的那个字母开始递归，这样次数会很少
        if cnt[word[-1]] < cnt[word[0]]:  # 优化二
            word = word[::-1]

        m, n = len(board), len(board[0])
        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:  # 匹配失败
                return False
            if k == len(word) - 1:  # 匹配成功！
                return True
            board[i][j] = ''  # 标记访问过
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 相邻格子
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True  # 搜到了！
            board[i][j] = word[k]  # 恢复现场
            return False  # 没搜到
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))








# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         #感觉用不太上
#         rows = len(board)
#         cols = len(board[0]) if rows > 0 else 0

#         vis = [[False for _ in range(cols)] for _ in range(rows)]
#         directions=[(1,0),(0,1),(-1,0),(0,-1)]

#         def dfs(index, i, j):
#             if index == len(word):
#                 return True
            
#             if i < 0 or i >= rows or j < 0 or j >= cols:
#                 return False
#             if board[i][j] != word[index]:
#                 return False
#             if vis[i][j]:
#                 return False
            
#             vis[i][j] = True
            
#             for dx, dy in directions:
#                 if dfs(index + 1, i + dx, j + dy):
#                     return True
            
#             vis[i][j] = False
#             return False
        

#         for row in range(rows):
#             for col in range(cols):
#                 ans=dfs(0,row,col)
#                 if ans==True:
#                     return True

#         return False




#这里逻辑错误，人家说了，不能回头！所以vis还是需要的
# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         rows = len(board)
#         cols = len(board[0]) if rows > 0 else 0

#         vis = [[False for _ in range(cols)] for _ in range(rows)]
#         directions=[(1,0),(0,1),(-1,0),(0,-1)]

#         def dfs(index,i,j):
            
#             if index==len(word):
#                 return True
#             vis[i][j]=True

#             ans=False
#             for dx,dy in directions:
#                 x=i+dx
#                 y=j+dy
#                 if 0<=x<rows and 0<=y<cols and board[x][y]==word[index] :
#                     print(board[x][y],word[index],ans)
#                     if dfs(index+1,x,y)==True and vis[x][y]==False:
#                         vis[x][y]==True
#                         ans=True
#                         break
#                     vis[x][y]==False

#             return ans
        

#         for row in range(rows):
#             for col in range(cols):
#                 ans=dfs(0,row,col)
#                 print(row,col)
#                 if ans==True:
#                     print(ans)
#                     return True

#         return False




# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """
#         #感觉用不太上
#         rows = len(board)
#         cols = len(board[0]) if rows > 0 else 0

#         vis = [[False for _ in range(cols)] for _ in range(rows)]
#         directions=[(1,0),(0,1),(-1,0),(0,-1)]

#         def dfs(index,i,j):
#             if index==len(word):
#                 return True
#             if vis[i][j]==True:
#                 return False
            
#             vis[i][j]=True
            
#             ans=False
#             #以后这种判断条件都放外面，放里面这乱七八糟的
#             # board = [["a"]]
#             # word = "a"
#             #第一次其实已经通过了，但是由于判断条件在循环内，他会再一次进行判断，进入下一次回溯，
#             #第二次时候，index=1,len(word)也等于1，但是由于循环的判断条件写在了循环内部，相当于他不会进入第二次循环，所以答案就一直ans默认的，是false
#             for dx,dy in directions:
#                 x=i+dx
#                 y=j+dy
#                 if 0<=x<rows and 0<=y<cols and board[x][y]==word[index] and vis[x][y]==False:
#                     print(board[x][y],word[index],ans)
#                     ans=dfs(index+1,x,y)
#                     if ans==True:
#                         break
#             vis[i][j]=False
#             return ans
        

#         for row in range(rows):
#             for col in range(cols):
#                 ans=dfs(0,row,col)
#                 if ans==True:
#                     print(ans)
#                     return True

#         return False

board = [["a"]]
word = "a"
solu=Solution()
print(solu.exist(board,word))