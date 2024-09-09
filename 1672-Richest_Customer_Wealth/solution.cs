public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int maxWealthSoFor = 0;
        foreach(int[] customers in accounts)
        {
            int currentCustomerWealth = 0;
            foreach (int bank in customers)
            {
                currentCustomerWealth += bank;
            }
            maxWealthSoFor = Math.Max(maxWealthSoFor, currentCustomerWealth);
        }
        return maxWealthSoFor;
    }//Time Complexity = O(m x n)
        //Space Complexity = O(1)
}