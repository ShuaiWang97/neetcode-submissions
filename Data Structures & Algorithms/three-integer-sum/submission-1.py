class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the nums
        # for each num, use two pointers to find sum of -num

        nums.sort()
        result=[]

        for i in range(len(nums)):
            if nums[i]>0:
                break
            
            # prevent duplict
            if i>0 and nums[i]==nums[i-1]:
                continue

            start=i+1
            end = len(nums)-1
            while start < end:
                if nums[start] + nums[end] > -nums[i]:
                    end -=1
                elif nums[start] + nums[end] < -nums[i]:
                    start +=1
                else:
                    result.append([nums[i],nums[start],nums[end]])

                    start += 1
                    end -= 1

                    # Skip duplicate pointer values
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    
                # print(result)

        return result