# Last updated: 15/5/2026, 10:12:01 p.m.
1class Solution(object):
2    def isPalindrome(self, x):
3        """
4        :type x: int
5        :rtype: bool
6        """
7        reverse_number = str(x)[::-1]
8
9        if reverse_number == str(x):
10            return True
11        
12        return False