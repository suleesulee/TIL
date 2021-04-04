class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans_list =[]
        ans=count.most_common(k)
        for i in range(k):
            ans_list.append(ans[i][0])
        return ans_list