class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans  = []
        
        for i in range(len(index)):
            ans.insert(index[i], nums[i])
            
        
        return ans
    



# answ2
    ans = []
    for i in range(len(nums)):
        if index[i] == len(target):
            ans.append(nums[i])
        else:
            target = ans[:index[i]] + [nums[i]] + ans[index[i]:]
            
    return ans