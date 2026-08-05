class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # use two for loops. one get prefix of product values before and one get values after
        #
        
        prefix_list = []
        value = 1
        for i in range(0, len(nums)):
            prefix_list.append(value)
            value *= nums[i]
        
        suffix_list=[]
        value =1
        for i in range(len(nums)-1,-1, -1):
            suffix_list.insert(0, value)
            value *= nums[i]

        return_list=[]
        for i in range(0, len(nums)):
            return_list.append(prefix_list[i]*suffix_list[i])

        return return_list