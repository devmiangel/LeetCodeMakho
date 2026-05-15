# Last updated: 15/5/2026, 3:44:57 a.m.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        node = ListNode()
        total_node = node

        while list1 and list2:
            
            if list1.val > list2.val:
                total_node.next = list2
                list2 = list2.next
            else:
                total_node.next = list1
                list1 = list1.next

            total_node = total_node.next
        
        if list1:
            total_node.next = list1
        else:
            total_node.next = list2




        return node.next

            
            