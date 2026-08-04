class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dict_ ={}
        for i in nums:
            if i in dict_.keys():
                return True
            else:
                dict_[i]=1
        return False
