class Solution {
    public boolean rotateString(String s, String goal) {
        String s2 = s + s;
        if (s2.contains(goal) && s.length() == goal.length())
            return true;
        else
            return false;
            
    }
}


//s를 두번더해 s안에 goal이 있는지 확인하는 방법.
//String의 contains, length 메소드