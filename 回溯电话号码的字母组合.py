#很奇妙的队列解法
class Solution(object):
    def letterCombinations(self,digits):
        if not digits:
            return []
        
        phone=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue=['']
        for digit in digits:
            print('digit:',digit)
            #一开始不为空，所以会进行一次
            for _ in range(len(queue)):
                print("_i :", _)
                #弹出，若为空，不影响
                #若不为空，正好输出了
                tem=queue.pop(0)
                print("tmp :",tem)
                for letter in phone[int(digit)-2]:
                    print("letter:",letter,"index:",int(digit)-2)
                    queue.append(tem+letter)
                    print("queue :", queue)
        return queue




#dfs
# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         if not digits:
#             return list()
        
#         map_list={"2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",}

#         conbination=[]
#         conbinations=[]

#         #每次从第index个数字里取一个字母
#         def dfs(index):
#             #停止条件,够两个就拼一块
#             if index == len(digits):
#                 conbinations.append("".join(conbination))

#             else:
#                 digit=digits[index]
#                 for letter in map_list[digit]:
#                     conbination.append(letter)
#                     dfs(index+1)
#                     conbination.pop()
        
#         dfs(0)

#         return conbinations
        



#不同怕麻烦，就当成树去做就可以，另外，可以直接定义对应关系！
# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], 
#            ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], 
#            ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        
#         numbers={str(i+2):chars for i,chars in enumerate(letters)}
#         result = list(digits)
#         ans=[]
#         for i in range(0,len(result)):
#             for key,value in numbers.items():
#                 # if result[i]==key:
#                 #     print(result[i],value)
#                 ans.append({result[i]:value for key,value in numbers.items() if result[i]==key})
#                 break
#         print(ans)

solu=Solution()
digits='23'
solu.letterCombinations(digits)