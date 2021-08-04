class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt, i = 0, 0
        
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1]==0) :
                flowerbed[i] = 1
                cnt += 1
            
            i += 1
        
        return cnt >= n

# 처음과ㄹ 마지막을 고려해서 꽃을 최대 몇개 심을 수 있는지 계산 
# 심어야하는 갯수보다 심을 수있는 자리가 많거나 같으면 Ture 아니면 False