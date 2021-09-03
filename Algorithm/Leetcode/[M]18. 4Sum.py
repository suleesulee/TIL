class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #두개 고르고 투포인터 고르고 하나를 옮김
        nums.sort()
        ans = []
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                s, e = j + 1, len(nums) - 1
                while s < e:
                    sum = nums[i] + nums[j] + nums[s] + nums[e]

                    if sum == target:
                        if sorted([nums[i], nums[j], nums[s], nums[e]]) not in ans:
                            ans.append([nums[i], nums[j], nums[s], nums[e]])

                    if sum < target:
                        s += 1
                    else:
                        e -= 1
        #print(ans)
        return ans
'''
투포인터 문제로 4개더하기 문제 

투 포인터로 풀었다.
문제는 4개라서 두개는 for문으로 움직이고 두개는 범위를 줄여가는 형태로 움직였음.
답인 배열을 만드는 부분에서 약간 당황함 
풀어내긴 했지만 해당 알고리즘은 시간 복잡도 측면에서 별로임 
고수들의 풀이에는 재귀가 담겨있었다...
 
'''    
