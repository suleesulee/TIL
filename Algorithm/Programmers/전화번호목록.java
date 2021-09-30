import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Map<String, Integer> m = new HashMap<>();
        for (String phone: phone_book){
            m.put(phone, 1);
        }
        
        //System.out.println(m);
        
        
        for (String phone: phone_book){
            for (int i = 1; i < phone.length(); i++){
                //System.out.println(phone_book[i].substring(0, j));
                if(m.containsKey(phone.substring(0, i))){
                    answer = false;
                    return answer;
                }
            }
        }
        return answer;
    }
}