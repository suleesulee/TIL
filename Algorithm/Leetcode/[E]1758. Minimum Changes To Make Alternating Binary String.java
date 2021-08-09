class Solution {
    public int minOperations(String s) {
        int cnt1 = 0;
        int cnt2 = 0;
        
        for (int i = 0; i < s.length(); i ++){
            if (i % 2 == 1){
                if (s.charAt(i) == '0'){
                    cnt1++;
                } else{
                    cnt2++;
                }
            } else {
                if (s.charAt(i) == '1'){
                    cnt1++;
                } else {
                    cnt2++;
                }
            }   
        }
        return Math.min(cnt1, cnt2);
        
    }
}

//String에서 특정 index의 문자를 가져올땐 charAt(index) 사용