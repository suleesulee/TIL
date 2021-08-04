class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_idx, word2_idx = [], []
        min_idx = 1e9
        
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                word1_idx.append(i)
            if wordsDict[i] == word2:
                word2_idx.append(i)
                
        
            
        for i in range(len(word1_idx)):
            for j in range(len(word2_idx)):
                min_idx = min(min_idx, abs(word1_idx[i]-word2_idx[j]))
        
        
        return min_idx
                