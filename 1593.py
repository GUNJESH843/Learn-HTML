class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        def dfs(i, cur):
            if i == len(s):
                return 0       
            ans = 0
            for j in range(i, len(s)):
                substr = s[i:j+1]
                if substr in cur:
                    continue
                cur.add(substr)
                ans = max(ans, 1+ dfs(j+1, cur))
                cur.remove(substr)
            return ans
        return dfs(0, set())