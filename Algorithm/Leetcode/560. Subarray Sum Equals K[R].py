'''
sol1인 brute force는 n^3 이라 결국 시간초과 나오는게 있음

sol2는 해시를 이용해 푸는방법
결국 리스트를 더해나가다 보면 
답이 될 수 있는 것은 현재까지 더한것에 k를 뺸 값이 있으면 된다라고 한다.
딕셔너리에 sum을 누적해서 기록하면서 key가 sum-k인 value 값이 있다면 더한다..

'''
#sol1

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum_nums = 0
        
        for i in range(len(nums)):
            sum_nums = 0
            for j in range(i, len(nums)):
                sum_nums += nums[j]
                if sum_nums == k:
                    ans += 1
                    break
        
        print(ans)
        return ans

#sol2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
            print(sums, d[sums], i)
        
        return count