import collections
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    #这个能过全部的
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0

        pre_sum=collections.defaultdict(int)
        #这里必须等于1，意思就是说当正好满足条件时，我要加上前面已有的
        #若初始化为0时，当路径和恰好等于目标和 targetSum 时，prev_sum - targetSum 的值为 0。此时，pre_sum[0] 的值为 0，算法会错误地认为没有满足条件的路径。
        #在这也就可以理解为前面还有一个虚拟结点，这样就可以从根节点开始计算
        pre_sum[0]=1

        def dfs(root,prev_sum):
            if not root:
                return 0
            
            #过不了
            #在这里，不能在更新前缀和之前计算新的前缀和，因为我们要算的是前缀和的结果，如果在这儿提前加上了，就会导致错误结果，逐步往后递归的结果就会出现错误
            #比如，当前缀和正好正与target的时候，因为pre_sum提前被设置为1，那么，此时的pre_sum[0]就会多加一个1，即便没有真的满足的条件
            #那为什么初始为1，但最后不会出错呢？因为在下面重新回溯到根节的时候，前缀和为0时，我们会重新减去一个！
            # prev_sum+=root.val
            # pre_sum[prev_sum] += 1
            # ret=0
            # ret+=pre_sum[prev_sum-targetSum]


            ret=0
            prev_sum+=root.val
            ret+=pre_sum[prev_sum-targetSum]
            pre_sum[prev_sum] += 1
            

            ret+=dfs(root.left,prev_sum)
            ret+=dfs(root.right,prev_sum)

            pre_sum[prev_sum]-=1

            return ret
        return dfs(root,0)



    #这样过不了一个案理   [1]  target=0
    # def pathSum(self, root, targetSum):
    #     if not root:
    #         return 0
    #     #前缀和记录的是，所有路径加起来等于key的路径有几个！
    #     pre_sum=collections.defaultdict(int)
    #     pre_sum[0]=1
        
    #     #自以为不需要判断，其实判断隐含在了ret += prefix[curr - targetSum]，字典中如果找不到，那就会返回0！
    #     def dfs(root,curr):
    #         if not root:
    #             return 0
    #         ret=0
    #         curr+=root.val
    #         ret += pre_sum[curr - targetSum]
    #         pre_sum[curr]+=1

    #         ret += dfs(root.left, curr)
    #         ret += dfs(root.right, curr)

    #         #前缀和哈希表的状态能够正确地反映当前路径的实际情况，避免对其他路径产生错误的影响
    #         #比如刚递归完某节点的左子树，要递归右子树了，那么在这时，属于左子树的前缀和必须要删除，否则就会影响右子树中的判断
    #         pre_sum[curr] -= 1

    #         return ret
    #     return dfs(root, 0)


    #❌❌❌❌❌到此的理解全部错误！一点不清晰，只对了一半
    # def pathSum(self, root, targetSum):
    #     if not root:
    #         return 0
    #     #前缀和记录的是，所有路径加起来等于key的路径有几个！
    #     pre_sum={}
    #     pre_sum[0]=1
        
    #     #下面的思想很危险，既然统计了前缀和，那就没必要计算是否等于targetSum！！！
    #     #❌同时，采用一个curr游标，来代表当前节点的前缀和,那么每一次只需要计算当前的前缀和加上游标即可判断够不够targetSum
    #     def dfs(root,curr):
    #         if not root:
    #             return 0
    #         #当前的等于targetSum的次数是0
    #         ret=0
    #         #计算一下加上本结点的前缀和，反正都要往下传，加了也没事
    #         curr+=root.val
    #         #❌!!!!!这一句非常的傻逼！因为我们已经不需要判断是否为8了，我们再遍历的过程中会把所有的前缀和都统计一边！！！所有情况！！
    #         #❌if curr==targetSum:

    #         pre_sum[curr]+=1
    #         pre_sum[root.val]+=1

            
            



    # def dfs(self,root,targetSum):
    #     if not root:
    #         return 0
    #     res=0

    #     if root.val == targetSum:
    #         res += 1

    #     res+=self.dfs(root.left,targetSum-root.val)
    #     res+=self.dfs(root.right,targetSum-root.val)

    #     return res



    # def pathSum(self, root, targetSum):
    #     if not root:
    #         return 0
        
    #     res=self.dfs(root,targetSum)
    #     #这里SB了，因为从其他节点开始的话，也必须保证结果等于8！！！
    #     res+=self.pathSum(root.left , targetSum)
    #     res+=self.pathSum(root.right , targetSum)
        
    #     return res



#遍历所有的路径，直接记录下来总和
#当前的想法，单词递归不可以，只能求出所有从根节点出发的满足条件的路径，而从其他结点出发的没法儿求出来

    # def pathSum(self, root, targetSum):
    #     if not root:
    #         return 0
        
    #     def dfs(root,targetSum):
    #         if not root:
    #             return 0
    #         res=0

    #         if root.val == targetSum:
    #             res += 1

    #         res+=dfs(root.left,targetSum-root.val)
    #         res+=dfs(root.right,targetSum-root.val)

    #         return res
        
    #     ans=dfs(root,targetSum)


head=TreeNode(3)
node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(5)
head.left=node1
head.right=node3
node1.right=node2

preorder = [3,9,20,15,7],
inorder = [9,3,15,20,7]
solu=Solution()
ans=solu.pathSum(preorder,inorder)

print(ans)