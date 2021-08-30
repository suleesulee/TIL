import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        for (String part: participant) {
            map.put(part, map.getOrDefault(part, 0) + 1);
        }
        
        for (String com: completion){
            map.put(com, map.get(com) - 1);
        }
        
        
        for (String key: map.keySet()){
            if(map.get(key) != 0) {
                answer = key;
            }
        }
        return answer;
    }
}

/*배운것 

getOrDefault() 메소드  
keySet() 메소드 - 모든 키를 가져옴 반복문에 넣어 돌리쟈

*/