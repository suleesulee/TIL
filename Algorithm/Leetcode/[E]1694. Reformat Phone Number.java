class Solution {
    public String reformatNumber(String number) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        
        number = number.replace("-", "").replace(" ", "");
        
        for (char c: number.toCharArray()){
            sb.append(c);
        }
        
        while (i < sb.length()-4){
            sb.insert(i+3, '-');
            i+=4;
        }
        
        if (sb.length() - i == 4)
            sb.insert(i+2, '-');
        
        return sb.toString();
                
    
    }
}

/*
일단.. 자바로 문자열 처리를 할수있는걸 배운걸로 큰 소득

StringBuilder를 사용해서 문자열 잘게 쪼개서 index마다 하나씩 '-' 문자 넣고

마지막 4개이하 남았을때만 처리해주면 됨..

toCharArray() 메소드는 하나의 캐릭터배열로 변경


*/