# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        elif not l1:
            return l2
        elif not l2:
            return l1
        
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
        
        n_node = ListNode()
        head = n_node
        for i in range(len(ans_list)):
            n_node.val = ans_list[i]
            if len(ans_list)-1 != i:
                n = ListNode()
                n_node.next = n
                n_node = n_node.next
           # print(head)
            

        return head