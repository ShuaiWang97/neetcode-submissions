class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        num_dict = {}
        for i in range(len(nums)):
            if nums[i] not in num_dict:
                num_dict[nums[i]]= i
            else:
                return True
        return False
        
        