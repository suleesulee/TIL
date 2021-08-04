class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        while right < len(chars):
            chars[left] = chars[right]
            cnt = 1
            while right + 1 < len(chars) and chars[right] == chars[right+1]:
                right += 1
                cnt += 1

            if cnt > 1:
                for idx in str(cnt):
                    chars[left+1] = idx
                    left +=1

            right += 1
            left += 1
        #print(chars)
        return left
        
        