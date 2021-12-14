// 앞이 나가지 못한다면 갇혀있음
// 100까지 채우면 기다림..

import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List<Integer> ans  = new ArrayList<>();
        Queue< Integer> pro = new LinkedList<>();
        Queue< Integer> sp = new LinkedList<>();
        int cnt = 0;
        
        for(int i = 0; i < progresses.length; i++){
            pro.offer(progresses[i]);
            sp.offer(speeds[i]);
        }
        
        System.out.println(pro);
        int day = 1;
        
        while(!pro.isEmpty()){
            int size = pro.size();
            while(pro.peek() + (sp.peek() * day) < 100){
                day++;
            }
            while (!pro.isEmpty() && pro.peek() + (sp.peek() * day)>=100){
                pro.remove();
                sp.remove();
                cnt ++;
            }
            if (cnt!= 0){
                ans.add(cnt);
                cnt = 0;
            }
        }
        
        answer = new int[ans.size()];
        for (int i = 0; i< ans.size(); i++){
            answer[i] = ans.get(i);
        }
        return answer;
    }
}