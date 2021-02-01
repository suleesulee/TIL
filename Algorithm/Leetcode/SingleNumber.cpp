class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int size = nums.size();
        
        if(size == 1){
            return nums[0];
        }
        
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i<size; i++){
            if(i == 0){
                if(nums[i] != nums[i+1])
                    return nums[i];
            }else if(i == size - 1){
                if(nums[i-1] != nums[i])
                    return nums[i];
            }else{
                if(nums[i]!=nums[i+1] &&nums[i-1]!=nums[i])
                    return nums[i];
            }
        }
        return -1;
    }
};