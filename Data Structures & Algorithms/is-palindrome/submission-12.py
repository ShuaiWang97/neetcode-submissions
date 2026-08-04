class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower() 
        # if len(s) == 1 or len(s) == 0:
        #     return True
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False

        return True
