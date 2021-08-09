# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        
        binary.append('0b')
        while head.next:
            binary.append(str(head.val))
            head = head.next
        binary.append(str(head.val))
        s_b = ''.join(binary)
        i_b = int(s_b, 2)
        
        return i_b
        
#파이썬의 내장함수들을 이용한 풀이