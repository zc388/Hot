def find_all_palindromic_substrings(s):
    res = []
    n = len(s)
    
    def expand_around_center(left, right):
        temp = []
        while left >= 0 and right < n and s[left] == s[right]:
            temp.append(s[left:right+1])
            left -= 1
            right += 1
        return temp
    
    for i in range(n):
        # 以单个字符为中心扩展
        res.extend(expand_around_center(i, i))
        # 以两个字符为中心扩展
        res.extend(expand_around_center(i, i+1))
    
    return res

# 示例
s = "aab"
print(find_all_palindromic_substrings(s))
# 输出: ['a', 'b', 'c', 'b', 'a', 'bcb', 'abcba']