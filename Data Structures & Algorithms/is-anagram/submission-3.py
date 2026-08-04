class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ala_dict = {}
        for i in range(len(s)):
            if s[i] not in ala_dict:
                ala_dict[s[i]]=1
            else:
                ala_dict[s[i]]+=1
        ala_dict2 = {}
        for i in range(len(t)):
            if t[i] not in ala_dict2:
                ala_dict2[t[i]]=1
            else:
                ala_dict2[t[i]]+=1
        print(ala_dict, ala_dict2)
        if ala_dict2 == ala_dict:
            return True
        else:
            return False
