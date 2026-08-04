class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict_={}
        for i in range(len(nums)):
            dict_[nums[i]] = i
        print(dict_)
        for i in range(len(nums)):
            difference = target - nums[i]
            print(difference)
            if difference in dict_.keys() and i!=dict_[difference]:
                return [i, dict_[difference]]
            
        