import java.util.*;
    
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> m = new HashMap<>();
        
        for (int i = 0; i < clothes.length; i++){
            String key = clothes[i][1];
            m.put(key, m.getOrDefault(key, 0) + 1);
        }
        
        for (int mValue : m.values()){
            //System.out.println(mValue);
            answer *= mValue + 1;
        }
        
        return answer - 1;
    }
}