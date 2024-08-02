class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        maxx = cnt = sum(nums[:k])
        n = len(nums)
        for i in range(k,n+k):
            cnt += nums[i % n]
            cnt -= nums[(i - k + n ) % n]
            maxx = max(maxx,cnt)
        
        return k - maxx