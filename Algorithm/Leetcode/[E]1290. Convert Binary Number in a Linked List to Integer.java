/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int num = head.val;
        while(head.next != null){
            num = num*2 + head.next.val;
            head = head.next;
        }
        return num;
    }
}

/*정석적인 풀이

배운점
1. 이진수에서 뒤에 하나 들어와서 밀리면 앞에서 계산한 값에서 *2 해주면 된다.

2. head.next!=null 이면 마지막 값을 못더하니깐 head.next.val을 사용하는것


*/