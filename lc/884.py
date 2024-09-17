class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sen1 = s1.split(' ')
        sen2 = s2.split(' ')
        words = sen1 + sen2
        return [word for word in words if words.count(word) == 1]