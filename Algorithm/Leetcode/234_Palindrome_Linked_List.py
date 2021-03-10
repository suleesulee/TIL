# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
20분 장고를 거듭하다 답을 봄
리스트로 옮겨와서 역순과 처음부터 값이 같은지 비교함
아주 파이써닉한 답인듯

나의 풀이는 노드의 갯수에 따라서 어떻게 홀짝 대처를 위해
모든 노드를 돌아 노드 수를 세려고함
노드 수를 나눈뒤 홀 짝을 나눠서 진행하려함

'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val = []
        c_node = head
        while c_node is not None:
            val.append(c_node.val)
            c_node = c_node.next
    
        return val == val[::-1]