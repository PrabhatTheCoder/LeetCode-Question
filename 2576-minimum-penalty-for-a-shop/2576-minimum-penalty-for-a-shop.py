class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        
        open_shop = [0] * (n + 1)
        close_shop = [0] * (n + 1)
        
        # Build prefix penalty: count of 'N' before index i
        for i in range(1, n + 1):
            if customers[i - 1] == 'N':
                open_shop[i] = open_shop[i - 1] + 1
            else:
                open_shop[i] = open_shop[i - 1]
                
        # Build suffix penalty: count of 'Y' after (and at) index i
        for i in range(n - 1, -1, -1):
            if customers[i] == 'Y':
                close_shop[i] = close_shop[i + 1] + 1
            else:
                close_shop[i] = close_shop[i + 1]
        
        min_penalty = float('inf')
        min_time = 0
        
        # Iterate over all possible closing times from 0 to n
        for i in range(n + 1):
            penalty = open_shop[i] + close_shop[i]
            if penalty < min_penalty:
                min_penalty = penalty
                min_time = i
                
        return min_time
