import math
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        #可以直接初始化为0
        max_profit=0
        for i,price in enumerate(prices):
            #这一段其实都可以用一句来代替
            # #当前的比上一个小，再和min_price对比，是不是最小
            # if i-1>=0 and prices[i]<prices[i-1]:
            #     if price<min_price:
            #         min_price=price
            min_price=min(min_price,price)
            profit=price-min_price
            max_profit=max(profit,max_profit)
        
        # if max_profit==-1:
        #     max_profit=0
        # print(max_profit)
        return max_profit
        # print(min_price,max_profit)

prices=[7,6,4,3,1]

solu=Solution()
solu.maxProfit(prices)