# Last updated: 15/5/2026, 3:44:58 a.m.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def RecLinkedList(self, lt):
 
        final_node = ListNode(lt[0])
        lt.pop(0)
        
        if len(lt) >= 1:
            final_node.next = self.RecLinkedList(lt)

        return(final_node)

    def addTwoNumbers(self, l1, l2):
        iterator_l1 = l1
        iterator_l2 = l2

        n1 = 0
        n2 = 0

        iteartion1 = 0
        iteartion2 = 0

        while (True):
            if iterator_l1.next == None:
                n1 += iterator_l1.val * pow(10, iteartion1)
                break
            else:
                n1 += iterator_l1.val * pow(10, iteartion1)
                iterator_l1 = iterator_l1.next
                iteartion1 += 1

        while (True):
            if iterator_l2.next == None:
                n2 += iterator_l2.val * pow(10, iteartion2)
                break
            else:
                n2 += iterator_l2.val * pow(10, iteartion2)
                iterator_l2 = iterator_l2.next
                iteartion2 += 1
        
        final_num = str(n1 + n2)
        num_arr = []

        for num in final_num:
            num_arr.append(int(num))
       
        num_arr.reverse()
        
        return self.RecLinkedList(num_arr)




        


        