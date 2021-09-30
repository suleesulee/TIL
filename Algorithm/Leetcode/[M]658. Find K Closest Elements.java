class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> cal_arr = new ArrayList<>();
        
        for(int num: arr){
            cal_arr.add(num);
        }
        
        Collections.sort(cal_arr, (num1, num2)-> Math.abs(num1 - x) - Math.abs(num2 - x));
        
        cal_arr = cal_arr.subList(0, k);
        Collections.sort(cal_arr);
        
        return cal_arr;
        
        
    }
}