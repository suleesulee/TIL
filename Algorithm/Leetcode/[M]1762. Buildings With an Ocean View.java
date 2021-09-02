class Solution {
    public int[] findBuildings(int[] heights) {
        Stack<Integer> stck = new Stack<>();
        int h_len = heights.length - 1;
        int cur = heights[h_len];

        for (int i = h_len; i >= 0 ; i--)
        {    
            if (stck.empty())
            {
                stck.add(i);
            } 
            else
            {
                 if(cur < heights[i])
                 {
                      cur = heights[i];
                      stck.add(i);
                 }
            } 
        }
        
        int[] ans = new int[stck.size()];
        int j = 0;
        while(!stck.empty()){
            ans[j] = stck.pop();
            j++;
        }
    return ans;
    }
}