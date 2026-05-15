# Last updated: 15/5/2026, 3:44:56 a.m.
class Solution(object):
    def isGood(self, nums):
        max_element = max(nums)
        num_len = len(nums)

        count_twice = 0
        cache_num = None
        value_duplicate = None

        if (max_element + 1 != num_len):
            return False
        
        for num in range(num_len) :
            for i in range(num, num_len):
                if nums[i] == cache_num:
                    count_twice += 1
                    value_duplicate = cache_num

            cache_num = nums[num]
            
            
            
        print(max_element, num_len, count_twice)

        if (count_twice != 1 or value_duplicate != max_element ): 
            return False
        return True


        