class Solution {
    public boolean isThree(int n) {
        int cnt = 1;
        
        for(int i = 2; i <= n; i++){
            if (n % i == 0)
                cnt++;
            if (cnt > 3)
                return false;
        }
        
        if (cnt == 3)
            return true;
        else 
            return false;
    }
}


# 너무 쉬운 문제가 아닌가 싶다
# 트릭이 딱히 없다