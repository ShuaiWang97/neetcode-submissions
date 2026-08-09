class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # sliding window problem. And use hash set to track which characters are currently in window for o(1) detection


        CharSet=set()
        l = 0
        set_=0

        for r in range(len(s)):

            while s[r] in CharSet:
                CharSet.remove(s[l])
                l +=1
            CharSet.add(s[r])

            set_= max(r-l+1, set_)

        return set_



        