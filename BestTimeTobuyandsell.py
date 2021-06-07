class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        cp=prices[0]
        
        for i in range(1,len(prices)):
            
            if prices[i] > cp:
                max_profit=max(max_profit ,(prices[i]-cp))
            else:
                cp=min(cp,prices[i])
        return max_profit
        
