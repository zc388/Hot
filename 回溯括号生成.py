#这里题，我陷入了一个超级大的误区，我在想他生成的过程，会不会出现这种)(())乱起暴躁的，就会想边判断，便递归，或者在长度够了的时候进行括号匹配

#正确想法，其实生成的过程是自己控制的，会让他先插入左括号，再插入右括号，当括号数目足够时，进行平衡判断即可！

#更正，上述方法没有误区！！！只是判断的方法总会想到复杂版的括号匹配，现在仍然是需要括号匹配，只是匹配的方法不同了

#暴力解
#由于两个要一人一半，所以可以根据左右括号的数量进行判断
#或者根据上一个括号1？
#优化
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        def dfs(path, left, right):
            # 当路径长度达到2n时，添加到结果中
            if len(path) == 2 * n:
                ans.append(path)
                return
            
            # 可以添加左括号的条件：左括号数量大于0
            if left > 0:
                dfs(path + '(', left - 1, right)
            
            # 可以添加右括号的条件：右括号数量大于左括号数量
            if right > left:
                dfs(path + ')', left, right - 1)
        
        dfs('', n, n)
        return ans




#需要转成字符串存放，除此之外，这个代码太过冗余，对比边界也没做处理，想想有没有别的方法
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         ans=[]
#         def dfs(Pare,left,right):
#             # print(Pare,left,right)
#             if len(Pare)==2*n:
#                 ans.append(''.join(Pare))
#                 return
        

#             if left>=right :
#                 Pare.append('(')
#                 dfs(Pare,left-1,right)
#                 Pare.pop()
#             else:
#                 if left>0:
#                     Pare.append('(')
#                     dfs(Pare,left-1,right)
#                     Pare.pop()
#                 Pare.append(')')
#                 dfs(Pare,left,right-1)
#                 Pare.pop()
#         dfs([],n,n)
#         print(ans)
#         return ans


#我这种写法，最终定格结果是这样
#[['(', '(', '(', ')', ')', ')'], ['(', '(', ')', '(', ')', ')'], ['(', '(', ')', ')', '(', ')'], ['(', ')', '(', '(', ')', ')'], ['(', ')', '(', ')', '(', ')']]
#但是我需要的是
#["((()))","(()())","(())()","()(())","()()()"]
#递归函数中使用列表Pare来构建括号组合，最后却将列表的浅拷贝添加到结果中，而题目要求返回字符串列表

# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         ans=[]
#         def dfs(Pare,left,right):
#             # print(Pare,left,right)
#             if len(Pare)==2*n:
#                 ans.append(Pare)
#                 return
        

#             if left>=right :
#                 Pare.append('(')
#                 dfs(Pare,left-1,right)
#                 Pare.pop()
#             else:
#                 if left>0:
#                     Pare.append('(')
#                     dfs(Pare,left-1,right)
#                     Pare.pop()
#                 Pare.append(')')
#                 dfs(Pare,left,right-1)
#                 Pare.pop()
#         dfs([],n,n)
#         print(ans)
#         return ans



solu=Solution()
solu.generateParenthesis(3)

ans='s'
ans+='a'
print(ans)