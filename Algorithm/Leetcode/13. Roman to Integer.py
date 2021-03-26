class Solution:
    def romanToInt(self, s: str) -> int:
        nums = []
        for i in range(len(s)):
            if s[i] == 'M':
                nums.append(1000)
            elif s[i] =='D':
                nums.append(500)
            elif s[i] =='C':
                nums.append(100)
            elif s[i] =='L':
                nums.append(50)
            elif s[i] =='X':
                nums.append(10)
            elif s[i] =='V':
                nums.append(5)
            elif s[i] =='I':
                nums.append(1)
        
        sum_nums = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                sum_nums -= nums[i]
            else:
                sum_nums += nums[i]
        
        sum_nums += nums[len(s)-1]
        return sum_nums
        
        #print(sum_nums)
        