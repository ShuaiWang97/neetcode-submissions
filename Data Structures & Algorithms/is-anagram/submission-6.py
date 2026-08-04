class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ## Time O(nlogn+mlogm) Space O(1)
        #return sorted(s) == sorted(t)

        ## They need to match both on the freq and elements
        ## Time complexity: O(n + m)
        ## Space  complexity: O(1) at most 26 alphabets
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1+ countS.get(s[i], 0)
            countT[t[i]] = 1+ countT.get(t[i], 0)
        
        return countT == countS

    