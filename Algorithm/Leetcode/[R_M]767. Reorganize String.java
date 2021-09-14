class Solution {
    public String reorganizeString(String s) {
        Map <Character, Integer> m = new HashMap<>();
        
        for (char ch: s.toCharArray()){
            m.put(ch, m.getOrDefault(ch, 0) + 1);
        }
        
        PriorityQueue <Map.Entry<Character, Integer>> max_pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        max_pq.addAll(m.entrySet());
        
        Map.Entry<Character, Integer> prevEntry = null;
        StringBuilder sb = new StringBuilder(s.length());
        
        while(!max_pq.isEmpty()){
            Map.Entry<Character, Integer> curEntry = max_pq.poll();
            
            if(prevEntry != null && prevEntry.getValue() > 0){
                max_pq.offer(prevEntry);
            }
        

            sb.append(curEntry.getKey());
            curEntry.setValue(curEntry.getValue() - 1);
            prevEntry = curEntry;
        }

    
        if(sb.toString().length() == s.length())
            return sb.toString();

        return "";
    }

    /*
    자바의 활용능력을 키우기위해 작업했다. 
    3-7 라인 빼고는 답을 보면서 작업함..
    Map.Entry를 사용해 반복하는 법을 배웠고
    람다를 사용해 Priorty q의 정렬을 맥스힙으로 변경하는것을 배움
    StringBuilder는 문장을 더할때 append
    자바로 푸는 연습을 열심히 해야한다.
    */