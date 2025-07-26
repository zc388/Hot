

class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        res=''
        mutil=0
        for c in s:
            if c.isdigit():
                mutil=mutil*10+int(c)
                #这里是说明，有需要重复的字符串了，遇到这种情况时才需要进栈
                #不进栈的直接用来相加就可以了，并且，每次将不需要进行相乘的和数字一起进栈
                #这样的话，每次从栈中弹出的有之前累积的括号外的数字和字母，括号外的字母就充当上一个字符，数字用来相乘
                #而遇到右括号之后，由于遇到左括号时，之前的东西都已经入栈，所以从左括号开始积累的字符都是需要相乘的
            elif c=='[':
                stack.append([mutil,res])
                #这里需要重置一下！
                res, mutil = "", 0
                #如果将要出栈，那么当前的这个元素不需要入栈，,并且前面的元素字符串直接出输加在现在的字符串上
            elif c==']':
                #这里其实不能用mutil，这样就相当于给他赋值了，下一次万一是数字，那就直接乘10了？
                cur_mutil,last_res=stack.pop()
                res=last_res+cur_mutil*res 
            else:
                res+=c
        return res






        # #有点脑瘫，现在的话这个样例过不了，需要思考一下 #"3[a2[c]]"
        # #每一次的结果都会重新清空，正常下的答案应该是"accaccacc"
        # #生成的是ccaaa
        #除此之外，还没办法应对数字，因为我的方法都是一位一位的，而题目的数字可不一定是个位，可能有十几个一起出现
       
        # ans=[]
        # result=''
        # # ans=['a','b']
        # # ans="".join(ans)

        # stack=[]
        # for str in s:
        #     if str.islower():
        #         stack.append(str)
        #     elif str.isdigit():
        #         stack.append(str)
        #     elif str=='[':
        #         stack.append(str)
        #     if str==']':

        #         #当前方法没办法解析内外嵌套的问题
        #         temp=[]
        #         while not stack[-1].isdigit():
        #             x=stack.pop()
        #             print(x)
        #             if x=='[':
        #                 continue
        #             temp.append(x)
        #         count=int(stack.pop())
        #         string="".join(temp[::-1])
        #         # print(count,string)
        #         for _ in range(0,count):
        #             result+=string
        #             print(string,result,_)
        #         ans.append(result)
                
        #         print("#####################")
                
        # return "".join(ans)







        #两个栈，分别存储数字和字符
        #遇到数字存数字，遇到字母存字母，如果字母上一个不是数字，那么同时向数字栈中存一个1
        #这个也不对！这个只能一一对应几次，能暴力但是不好调整括号内外，到外面写起来也很麻烦，所以还得是用栈
        #我觉得，遇到数字，左括号和字母就入栈，遇到右括号就一直出栈到第一个数字，这样的话就是数字*字母拼接
        # for i,str in enumerate(s):
        #     if str.isdigit():
        #         numb.append(int(str))
        #         last_char=str
        #         #有个函数叫做char.islower()
        #         #有个函数叫做char.isdigit()
        #     elif str.islower():
        #         if not last_char.isdigit():
        #             print(str,1)
        #             numb.append(1)
        #         char.append(str)
        #         last_char=str
        #     else:
        #         continue
        
        # print(numb)
        # print(char)
        










s = "3[a]2[bc]"
solu=Solution()
print(solu.decodeString(s))