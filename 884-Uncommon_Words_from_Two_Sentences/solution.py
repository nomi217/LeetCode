class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_count = Counter(s1.split())
        s2_count = Counter(s2.split())
        combined_count = s1_count + s2_count
        unique_words = []
        for word, count in combined_count.items():
            if count == 1:
                unique_words.append(word)
        return unique_words
        # Time Complexity = O(m+n)
        # Space Complexity = O(m+n)