class Solution {
    public int solution(String s) {
        int answer = 12345678;
        String res = "";
        
        if (s.length() == 1){
            return 1;
        }
        
        //1, 2, 3, 4,...
        //0-2, 2-4, 4-6...
        
        for(int i = 1; i <= s.length() / 2 + 1; i++){
            int count = 1;
            String now = "";
            String next = "";

            for (int j = 0; j <= s.length() / i; j++){
                int start = j * i;
                int end = i * (j+1) > s.length() ? s.length() : i *(j+1);
                now = next;
                next = s.substring(start, end);
                
                if(now.equals(next)){
                    count++;
                } else{
                    if(count == 1){
                        res += now;
                    } else {
                        res += Integer.toString(count) + now;
                    }
                    count = 1;
                }
            }
            if(count == 1){
                res += next;
            } else {
                res += Integer.toString(count) + next;
            }
            //System.out.println(res);
            answer = Math.min(answer, res.length());
            res = "";

        }
                
                    
        return answer;
    }
}