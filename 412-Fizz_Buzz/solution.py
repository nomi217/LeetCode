class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range (1,n+1):
            divisibleby3 = i % 3 == 0
            divisibleby5 = i % 5 == 0

            currStr = ""
            if divisibleby3:
                currStr += "Fizz"
            if divisibleby5:
                currStr += "Buzz"
            if not currStr:
                currStr += str(i)

            answer.append(currStr)
        return answer