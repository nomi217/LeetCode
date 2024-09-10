class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealthSoFar = 0
        for customers in accounts:
            currentCustomerWealth = 0
            for banks in customers:
                currentCustomerWealth +=banks
            maxWealthSoFar = max(maxWealthSoFar, currentCustomerWealth)
        return maxWealthSoFar
        
        #Time Complexity = O(m x n)
        #Space Complexity = O(1)