class Solution {
    public int[] shuffle(int[] nums, int n) {
        
        int[] left = new int[n];
        int[] right = new int[n];
        int[] ans = new int[n*2];
        int j = 1;
        int k = 0;
        
        for (int i = 0; i < nums.length ; i++){
            if (i < n){
                left[i] = nums[i];
            } else {
                right[i-n] = nums[i];
            }
            
        }
        
        // System.out.println(right[0]);
        // System.out.println(right[1]);
        // System.out.println(right[2]);

        
        ans[0] = left[0];
        for(int i = 1; i < nums.length; i++){
            if(i%2 == 0){
                ans[i] = left[j];
                j++;
            } else {
                ans[i] = right[k];
                k++;
            }
            
        }
        
        System.out.print(ans);   
        return ans;
    }
}


// 더 나은 풀이

class Solution2 {
    public int[] shuffle(int[] nums, int n) {
        
        int[] res = new int[2*n];
        int j = 0;
        for (int i = 0; i< n; i++){
            res[j++] = nums[i];
            res[j++] = nums[i+n];

        }

        return res;
    }
}