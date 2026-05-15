# Last updated: 15/5/2026, 3:44:59 a.m.
class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            fist = nums[i]
            for j in range(i+1, len(nums)):
                if fist + nums[j] == target:
                    return [i,j]
