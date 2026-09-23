class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        left = 0

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False
        