class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #先排序，保证大小顺序，同时将相同的数字相邻
        candidates.sort()
        ans=[]
        def dfs(count,path,start,target):
            # if count>target:
            #     return
            #在这里添加一个开始序列，用于控制从哪里开始回溯，这样就可以有效的控制重复循环
            #不加的时候，2->3   加了之后2->3, 下一次从3开始，3只能往后遍历
            if target==0:
                # print(path)
                ans.append(path.copy())
            
            for i in range(start,len(candidates)):
                
                can=candidates[i]
                if target-can<0:
                    break
                path.append(can)
                count+=can
                dfs(count,path,i,target-can)
                path.pop()
                count-=can
        dfs(0,[],0,target)
        return ans
    
#选或不选的方案，这个更巧妙，省去了循环的内容
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            if i == len(candidates) or left < candidates[i]:
                return

            # 不选
            dfs(i + 1, left)

            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()  # 恢复现场

        dfs(0, target)
        return ans


    
# #K神的另一种写法，速度会更快,循环时进行剪枝，会少遍历很多个边
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         def backtrack(
#             state: list[int], target: int, choices: list[int], start: int, res: list[list[int]]
#         ):
#             """回溯算法：子集和 I"""
#             # 子集和等于 target 时，记录解
#             if target == 0:
#                 res.append(list(state))
#                 return
#             # 遍历所有选择
#             # 剪枝二：从 start 开始遍历，避免生成重复子集
#             for i in range(start, len(choices)):
#                 # 剪枝一：若子集和超过 target ，则直接结束循环
#                 # 这是因为数组已排序，后边元素更大，子集和一定超过 target
#                 if target - choices[i] < 0:
#                     break
#                 # 尝试：做出选择，更新 target, start
#                 state.append(choices[i])
#                 # 进行下一轮选择
#                 backtrack(state, target - choices[i], choices, i, res)
#                 # 回退：撤销选择，恢复到之前的状态
#                 state.pop()

#         state = []  # 状态（子集）
#         candidates.sort()  # 对 candidates 进行排序
#         start = 0  # 遍历起始点
#         res = []  # 结果列表（子集列表）
#         backtrack(state, target, candidates, start, res)
#         return res


    #现在的写法不错，但是会存在重复组合，所以需要去重！
    # [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]
    # def combinationSum(self, candidates, target):
    #     """
    #     :type candidates: List[int]
    #     :type target: int
    #     :rtype: List[List[int]]
    #     """

    #     ans=[]
    #     def dfs(count,path):
    #         if count>target:
    #             return
            
    #         if count==target:
    #             ans.append(path.copy())
            
    #         for can in candidates:
    #             path.append(can)
    #             count+=can
    #             dfs(count,path)
    #             path.pop()
    #             count-=can
    #     dfs(0,[])
    #     print(ans)


candidates = [2,3,6,7]
target = 7
solu=Solution()
print(solu.combinationSum(candidates,target))


















        



# #4.1 枚举所有集合
# # n=3
# # for s in range(1 << n):
# #     print(s)

# #4.2 枚举非空子集
# #在这必须要明确，二进制的子集，就是子集中，任何为1的一位，在原数中的对应位必须也为1，0则无所谓
# #判断条件   a & s == a
# # s=0b10101
# # sub = s
# # while sub:
# #     # 处理 sub 的逻辑
# #     print(bin(sub))
# #     sub = (sub - 1) & s
    


# # §4.3 枚举子集（包含空集）
# s=0b10101
# sub = s
# while True:
#     # 处理 sub 的逻辑
#     if sub == 0:
#         break
#     sub = (sub - 1) & s
#     print(bin(sub))
