class Solution: #define the class
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int: #define the function
        pf = {} #initialize the dictionary

        for i in arr1: #iterate through the first array
            str1 = str(i)  #convert the integer to string
            prefix = "" #initialize the prefix
            for n in str1: #iterate through the string
                prefix += n #add the character to the prefix
                pf[prefix] = pf.get(prefix, 0) + 1 #add the prefix to the dictionary
            maxlength = 0 #initialize the maximum length of the prefix

        for j in arr2: #iterate through the second array
            str2 = str(j) #convert the integer to string
            prefix = ""     #initialize the prefix
            for m in str2: #iterate through the string
                prefix += m     #add the character to the prefix
                if prefix in pf: #if the prefix is in the dictionary
                    maxlength = max(maxlength,len(prefix)) #update the maximum length of the prefix
        return maxlength #return the maximum length of the prefix

