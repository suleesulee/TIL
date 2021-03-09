# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p_node = None
        c_node = head
        while c_node:
            n_node = c_node.next
            c_node.next = p_node
            p_node = c_node # p_node에 c_node를 대입하는 순간 c_node의 val과 c_node의 next를 주목해야함 위에서 c_node.next는 p_node임 결국 \
            c_node = n_node # c_node를 p_node에 대입하는건 c_node의 새로운 v값과 c_node.next가 p_node 인것
            #print(p_node)
        head = p_node
        return head