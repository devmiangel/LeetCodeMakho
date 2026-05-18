# Last updated: 17/5/2026, 11:55:59 p.m.
1class Solution(object):
2    def rotateString(self, s, goal):
3        total_string = s + s
4
5        if len(s) != len(goal): return False
6
7        return goal in total_string
8            
9
10
11
12
13
14
15        
16        