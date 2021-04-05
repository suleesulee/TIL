# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        heapBSet = set()

        while headB:
            heapBSet.add(headB)
            headB = headB.next

        while headA:
            if headA in heapBSet:
                return headA
            headA = headA.next

        return None