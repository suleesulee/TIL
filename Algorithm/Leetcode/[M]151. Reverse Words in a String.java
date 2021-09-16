import java.util.Arrays;

class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        List<String> ans = Arrays.asList(s.split("\\s+"));
        Collections.reverse(ans);

        return String.join(" ", ans);

    }
}

/**
 * Medium
 * 그냥 내부 메소드를 얼마나 잘쓰나 자바는 정규식 알고있나 문제인것 같다.
 *  Arrays.asList(T...a)
 *  이런식으로 리스트에 때려넣고
 *  Collections.reverse를 이용하여 돌린다. 
 *  String.join(" ", ans) 까지 활용하면 금상첨화
 * 
 */