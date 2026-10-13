class Solution(object):
    def summaryRanges(self, nums):
        result = []

        if len(nums) == 0:
            return result

        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[right - 1] + 1:
                if left == right - 1:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left]) + "->" + str(nums[right - 1]))

                left = right

        if left == len(nums) - 1:
            result.append(str(nums[left]))
        else:
            result.append(str(nums[left]) + "->" + str(nums[-1]))

        return result