# Time-complexity - O(n)
# Space-complexity - O(1)
def maxProfit(prices):
    max_profit = 0
    min_price = float("inf")
    
    for price in prices:
        min_price = min(price, min_price)
        
        profit = price - min_price
        
        max_profit = max(max_profit, profit)
        
    return max_profit

# Example usage
prices = [7, 1, 5, 3, 6, 4]
print("Maximum Profit:", maxProfit(prices))  # Output: 5