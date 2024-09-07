public class Solution {
    public int[] RunningSum(int[] nums) {
        for(int i=1;i<nums.Length;i++)
        {
            nums[i] = nums[i-1] + nums[i];
        }
        return nums;
    }//time complexity is O{n}
     //space complexty is O(n) because declare an array result of size n to store the running sum and access the previous value to calculate the next value
}