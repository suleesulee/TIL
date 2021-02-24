#easy
#python3
#two pointer

class Solution:
    def hasCycle(self, head: ListNode) -> bool:     # head는 ListNode 형
        slow = fast = head  #slow, fast 모두 헤드를 가르킴
        while fast and fast.next:   # fast의 next가 없으면 반복문 탈출, and는 c의 &&
            slow, fast = slow.next, fast.next.next  
            
            if slow == fast:    #후위로 따라오는 값과 하나 앞의 값이 같다  = 순환한다.
                return True
        
        return False