public class Solution {
    public IList<string> FizzBuzz(int n) {
        List<string> answer = new List<string>();

        for (int i = 1; i <= n; i++)
        {
            bool divisibleby3 = i % 3 == 0;
            bool divisibleby5 = i % 5 == 0;

            string currStr = "";
            if(divisibleby3)
            {
                currStr += "Fizz";
            }
            if(divisibleby5)
            {
                currStr += "Buzz";
            }
            if(currStr.Equals(""))
            {
                currStr = i.ToString();
            }
            answer.Add(currStr);
        }
        return answer;
    }//Time Complexity = O(n)
    //Space Complexity = O(1)
}