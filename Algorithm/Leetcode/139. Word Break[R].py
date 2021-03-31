class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recur(s:str, word_dict:Set[str], start:int):
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                #print(s[start:end])
                if s[start:end] in word_dict and recur(s, word_dict, end):
                    return True
            return False
        return recur(s, set(wordDict), 0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        q = deque()
        visited = set()

        q.append(0)
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    q.append(end)
                    if end == len(s):
                        return True
                visited.add(start)
        return False