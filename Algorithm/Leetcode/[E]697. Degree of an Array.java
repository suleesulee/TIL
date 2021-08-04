class Solution {
    private class Data{
        int left;
        int right;
        int cnt;
        
        public Data(int left, int right, int cnt){
            this.left = left;
            this.right = right;
            this.cnt = cnt;
        }
        
    }
    
    public int findShortestSubArray(int[] nums) {
        Map<Integer, Data> info = new HashMap<>();
        int maxFreq = 1;
        
        for(int i = 0; i < nums.length; i++){
            int n = nums[i];
            if(!info.containsKey(n)){
                Data d = new Data(i, i, 1);
                info.put(n, d);
            } else {
                Data getData = info.get(n);
                Data d = new Data(getData.left, i, getData.cnt + 1);
                info.put(n, d);
                maxFreq = Math.max(maxFreq, getData.cnt + 1); 
            }
        }
        
        int ans = Integer.MAX_VALUE;
        for(Integer key: info.keySet()){ 
            Data d = info.get(key);
            if(maxFreq == d.cnt)
                ans = Math.min(ans, d.right - d.left + 1);                
        }
        return ans;
    }
}

//데이터를 담을 객체를 만들어 선언해라
//Map의 메소드 사용법 containsKey(), keySey(), put(), get()
//Integer.MAX_VALUE
//Math Class의 min, mat 메소드