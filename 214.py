class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]  #reverse the string
        l = s + "#" + rev_s #add both normal and reverse string
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            if l[i] == l[j]:
                j += 1
            p[i] = j
        return rev_s[:len(s) - p[-1]] + s