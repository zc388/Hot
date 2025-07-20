def permute(nums):
    result = []
    n = len(nums)
    
    def backtrack(path, used):
        # 当路径长度等于原数组长度时，说明找到了一个全排列
        if len(path) == n:
            result.append(path.copy())
            return
        
        # 遍历所有可能的选择
        for i in range(n):
            # 如果当前数字已经在路径中，跳过
            if used[i]:
                continue
            
            # 做选择
            path.append(nums[i])
            used[i] = True
            
            # 进入下一层决策树
            backtrack(path, used)
            
            # 撤销选择
            path.pop()
            used[i] = False
    
    # 记录数字是否被使用过
    used = [False] * n
    backtrack([], used)
    
    return result

# 示例用法
if __name__ == "__main__":
    nums = [1, 2, 3]
    print("全排列结果：")
    for perm in permute(nums):
        print(perm)