class Solution:  
    def longestStrChain(self, words: List[str]) -> int:
        memo = {word:None for word in words}
        
        print(memo)
        
        def dfs(curr):
            if curr not in memo:
                return 0
            result = 0
            if not memo[curr]:
                for i in range(len(curr)):
                    #print(curr[:i] + curr[i+1:])
                    result = max(result, 1 + dfs(curr[:i] + curr[i+1:]))
                memo[curr] = result
            return memo[curr]

        total = 0
        for word in memo:
            total = max(total, dfs(word))
        return total
'''
Medium
DP + DFS 결합 문제

끝내주는 DFS방법이다. 와우..
한문장에서 하나씩 뺴버리는 방법은 꼭외우자
dfs(curr[:i] + curr[i+1:])

'''