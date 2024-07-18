class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## Approch one using frequency count in hash table
        """
        freq_count = {}
        n = len(nums)
        for num in nums:
            freq_count[num] = freq_count.get(num,0) + 1
        
        for num, count in freq_count.items():
            if count > n//2:
                return num
        
        return -1"""
        ## Approach two using Boyer-Moore Majority Vote Algorithm
        count = 1
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i] != ans:
                count-=1
            else:
                count+=1

            if count ==0:
                ans = nums[i]
                count = 1

        return ans
