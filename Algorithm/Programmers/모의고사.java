import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        int[] s1 = {1,2,3,4,5};
        int[] s2 = {2,1,2,3,2,4,2,5};
        int[] s3 = {3,3,1,1,2,2,4,4,5,5};
        int cnt1 = 0;
        int cnt2 = 0;
        int cnt3 = 0;
        
        for (int i = 0; i<answers.length; i++){
            if(s1[i%s1.length] == answers[i])
                cnt1++;
            if(s2[i%s2.length] == answers[i])
                cnt2++;
            if(s3[i%s3.length] == answers[i])
                cnt3++;
        }
        
        int max_cnt = Math.max(Math.max(cnt1, cnt2), cnt3);
        List<Integer> ans = new ArrayList<>();
            
        
        if (max_cnt == cnt1){
            ans.add(1);
        }
        
        if (max_cnt == cnt2){
            ans.add(2);
        }
        
        if (max_cnt == cnt3){
            ans.add(3);
        }
        
        int size = 0;
        answer = new int[ans.size()];

        for(Integer tmp : ans){
            answer[size++] = tmp;
        }        
        return answer;
    }
}