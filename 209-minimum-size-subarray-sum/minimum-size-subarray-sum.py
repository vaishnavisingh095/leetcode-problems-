class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        sum = 0 
        min_length = float('inf')
        for right in range (len(nums)):
            sum += nums[right]
            while sum >= target:
                min_length= min([min_length,right-left+1])
                sum -=nums[left]
                left +=1
        if min_length == float('inf'):
            return 0
        
        return min_length

                

               