class Solution:

    def encode(self, strs: List[str]) -> str:


        # Solution 1: size + "," +# + strs
        if not strs:
            return ""

        size_list = []
        coded=""

        for str_ in strs:
            size_list.append(len(str_))

        for size in size_list:
            coded += str(size) + ","
        coded +="#"
        for str_ in strs:
            coded +=str_

        print("coded: ",coded)
        return coded
        


    def decode(self, s: str) -> List[str]:
        if not s:
            return list("")
        
        # get the size
        i=0
        size_list=[]
        while s[i]!="#":
            j = i
            while s[j]!= ",":
                j+=1
            size = s[i:j]
            i = j+1
            size_list.append(size)
        
        i += 1
        str_list=[]
        for size in size_list:
            str_list.append(s[i:i+int(size)])
            i= i+int(size)

        
        return list(str_list)



