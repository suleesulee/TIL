class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        nums1.sort()
        nums2.sort()
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    nums2[j] = -1
                    break
        
        return res
    
    

#O(n^2)

# 다른 답 투포인터
# O(nlogn)


i, j = 0
res = []
nums1.sort()
nums2.sort()
while i <len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        i += 1
        continue
    if nums1[i] > nums2[j]:
        j += 1
        continue
    
    res.append(nums1[i])
    i+=1
    j+=1
    
return res