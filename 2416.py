class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Create a trie data structure to store the prefixes
        trie = {}
        result = []  
        
        # Build the trie by counting prefix occurrences
        for word in words: 
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {'count': 0}
                node = node[char]
                node['count'] += 1
        
        # Calculate the prefix score for each word
        for word in words:
            node = trie
            score = 0
            for char in word:
                node = node[char]
                score += node['count']
            result.append(score)
        
        return result
