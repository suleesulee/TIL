# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list, l2_list = [], []
        ans_Node = ListNode(0)
        head = ans_Node
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
            
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        
        l1_list.reverse()
        l2_list.reverse()
        
        for i in range(len(l1_list)):
            l1_list[i] = str(l1_list[i])
            
        for i in range(len(l2_list)):
            l2_list[i] = str(l2_list[i])
            
        ans = int(''.join(l1_list)) + int(''.join(l2_list))
        
        ans_list = list(str(ans))
        
        for i in reversed(range(len(ans_list))):
            head.next = ListNode(0)
            head.next.val = ans_list[i]
            head = head.next
        
        return ans_Node.next