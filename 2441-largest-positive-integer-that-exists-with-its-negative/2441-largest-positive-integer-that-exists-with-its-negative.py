class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg_set = set()

        # Loop through the list and insert absolute values of negtive elements in the set
        for num in nums:
            if num<0:
                neg_set.add(-num)
        
        max_k = -1

        #Iterate through numbers to find the maximum positive integer 
        for num in nums:
            if num > max_k and num in neg_set:
                max_k = num

        return max_k