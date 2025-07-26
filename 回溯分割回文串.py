class Solution(object):
    #选或不选下一个
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path=[]
        result=[]
        def dfs(end,strat):
            if end==len(s):
                result.append(path.copy())
                return
            print(end,strat)
            #如果选下一个，也就是长度扩充一个
            #一开始会直接回溯到底，直接搞成最长的，然后一点点往后缩
            if end<len(s)-1:
                dfs(end+1,strat)

            #走到这儿，那就是当前的选了，不选下一个，那就该判断一下了
            #注意，如果不选下一个，那么自然下一个要有新得起点和终点
            #如果满足，那就直接标记
            print(s[strat:end+1])
            if s[strat:end+1]==s[strat:end+1][::-1]:
                
                path.append(s[strat:end+1])
                dfs(end + 1, end + 1)
                path.pop()
        
        dfs(0,0)
        print(result)
        return result




# class Solution(object):
#     #回溯
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """
#         result = []
#         path = []
#         length = len(s)
#         # 其实，回溯的精髓就在于动态的进行选择，你要选择还是不要选择你面前的这个元素，如果满足了条件，那你就选择它，如果不满足，那你就不要她
#         def dfs(index):
#             if index >= length:
#                 result.append(path.copy())
#                 return
#             for i in range(index, length):
#                 substring = s[index:i+1]
#                 print(substring)
#                 if substring == substring[::-1]:
#                     path.append(substring)
#                     print(path,index,i)
#                     print("#########")
#                     dfs(i + 1)
#                     # 回溯，移除最后添加的子串，尝试其他可能
#                     path.pop()
        
#         dfs(0)
#         print(result)
#         return result



solu=Solution()
s = "aab"
solu.partition(s)