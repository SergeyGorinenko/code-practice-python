"""
Leetcode 121. Best Time to Buy and Sell Stock
Level: Easy
Memory: O(1)
Time: O(n)

You are given an array prices where prices [i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
• 1 ≤ prices.length ≤ 10^5
• 0 ≤ prices[i] ≤ 10^4
"""

class BestTimeToBuyAndSellStock(object):

    id = 'Leetcode 121. Best Time to Buy and Sell Stock'

    def maxProfit(self, prices):
        profit = 0
        minPrice = float('inf')
        for index, price in enumerate(prices):
            if price < minPrice:
                minPrice = price
            else:
                if price - minPrice > profit:
                    profit = price - minPrice
        return profit

instance = BestTimeToBuyAndSellStock()

nums1 = [7,1,5,3,6,4]
result1 = instance.maxProfit(nums1)
print(f'{nums1}: {result1}')

nums2 = [7,6,4,3,1]
result2 = instance.maxProfit(nums2)
print(f'{nums2}: {result2}')
