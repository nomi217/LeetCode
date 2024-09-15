class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        for i in range(len(s), 0, -1):
            for j in range(len(s) - i + 1):
                sub = s[j: j + i]
                has_old_vowel = False
                for vowel in ['a','e','i','o','u']:
                    if sub.count(vowel) % 2 != 0:
                        has_old_vowel = True
                        break
                if not has_old_vowel:
                        return i
        return 0
        # Time complexity: 𝑂(𝑛3)
        # Space complexity: 𝑂(1)
