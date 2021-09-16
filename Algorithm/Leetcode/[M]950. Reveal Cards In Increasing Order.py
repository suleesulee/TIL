class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        idx = collections.deque(range(n))
        ans = [0] * n
        
        for card in sorted(deck):
            #print(idx)

            ans[idx.popleft()] = card
            #print(ans)
            if idx:
                idx.append(idx.popleft())
        
        return ans
    
'''
Medium


'''