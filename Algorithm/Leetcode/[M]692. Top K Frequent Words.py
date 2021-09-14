class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_cnt = Counter(words)
        ans = []
        word_cnt_list = [(v, k) for k, v in word_cnt.items()]
        
        #print(word_cnt_list)
        
                
        word_cnt_list.sort(key=lambda x: (-x[0], x[1]))
        
        #print(word_cnt_list)
        for i in range(k):
            ans.append(word_cnt_list[i][1])
        
        
        return ans
        
        
'''
간단히 풀었다..
그냥 쭉 풀어서 풀어낸거기에 어렵지 않았다.
'''