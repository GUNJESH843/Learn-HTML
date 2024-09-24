class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pf = {}

        for i in arr1:
            str1 = str(i)
            pre = ""
            for n in str1:
                pre += n
                pf[pre] = pf.get(pre, 0) + 1
            maxl = 0

        for j in arr2:
            str2 = str(j)
            pre = ""
            for m in str2:
                pre += m
                if pre in pf:
                    maxl = max(maxl,len(pre))
        return maxl

