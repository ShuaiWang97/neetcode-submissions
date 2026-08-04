class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # write a help function on checking Anagrams
        # Then with hash map do a for loop to add list

        # def Anagrams(a , b):
        #     return sorted(a) == sorted(b)
        
        # map_={}
        # for i in strs:
        #     for j in map_.keys():
        #         if Anagrams(i , j):
        #             map_[j].append(i)
        #         else:
        #             map_[i]=[i]
        # print(map_)
        # return list(map_.values())

        groups={}
        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key]=[]
            
            groups[key].append(word)

        return list(groups.values())

        
