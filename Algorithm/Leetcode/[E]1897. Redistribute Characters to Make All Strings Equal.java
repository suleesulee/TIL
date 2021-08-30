class Solution {
    public boolean makeEqual(String[] words) {
        Map<Character, Integer> m  = new HashMap<>();
        
        for(int i = 0; i <words.length; i++){
            for(int j = 0; j < words[i].length(); j++){
                char c =  words[i].charAt(j);
                m.put(c, m.getOrDefault(c, 0) + 1);
            }
        }
               
        
        for (char key: m.keySet()){
            if(m.get(key) % words.length != 0)
                return false;
        }
        return true;
    }
}

/* 
파이썬으로 푼 방식과 동일하게 풀었다. 
9ms
다만 자바로 푸는 방식은 빠르게 푼 사람들이 존재해서 그사람들 답을 보니
배열에다가 증가 때려넣고 마지막에 비교하는 형식으로 풀었음;;
해시맵을 사용하지 않았음
1차적으로 모든 단어의 길이를 더한 값과 단어 갯수가 나누어 떨어지는지 보고
위 방식을 배열에 적용하여 배열값을 단어 갯수와 나눠봄

charAt(index)
put(K,V)
getOrDefault(K, {default_value}):
keySet() iter할때 사용
get(K) key에 따른 Value가져옴 

toCharArray(): String을 char배열로 바꿔준다.


*/