# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_list = []
        l2_list = []
        
        while l1:
            l1_list.append(str(l1.val))
            l1 = l1.next
        while l2:
            l2_list.append(str(l2.val))
            l2 = l2.next
            
        l1_str = ''.join(l1_list)
        l2_str = ''.join(l2_list)
        
        ans = int(l1_str) + int(l2_str)
        ans_list = list(str(ans))
        #print(ans_list)
        
        nNode = ListNode()
        head = nNode
        for i in ans_list:
            nNode.val = i
            n = ListNode()
            nNode.next = n
            nNode = n
            
        print(head)
        
        return head