class Solution {
    public int findPeakElement(int[] nums) {
        return search(nums, 0, nums.length-1);
    }
    public int search(int[] nums, int l, int r){
        if (l==r)
            return l;
        int mid = (l+r) /2;
        if (nums[mid] > nums[mid + 1])
            return search(nums, l, mid);
        return search(nums, mid+1 ,r);
    }
    
}

/*
파이썬은 선형탐색으로 자바는 이진탐색으로 답을 구했다..
나는 선형탐색 더빠른 방법은 이진탐색이었다..

피크점을 찾아서 계속해서 이진탐색하는 방법으로 현재값이 뒷값보다 크면 앞부분으로 이동해서 이진탐색
반대의 경우는 뒷부분을 찾아 이진탐색하여 피크점을 찾아냄

중간값을 구하고 앞뒤로 이동하는 기준만 정해줬다면 아주 빠르게 풀 수 있었던 문제
 */