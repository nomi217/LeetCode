class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def dfs(exp):
            if exp.isdigit():
                return [int(exp)]
            ans = []
            for i, c in enumerate(exp):
                if c in '-+*':
                    left, right = dfs(exp[:i]), dfs(exp[i +1:])
                    for a in left:
                        for b in right:
                            if c == '-':
                                ans.append(a - b)
                            elif c == '+':
                                ans.append(a + b)
                            else:
                                ans.append(a * b)
            return ans
        return dfs(expression)
       #Time Complexity: O(2n) where n is the number of digits.
       # Space Complexity: O(n+m)