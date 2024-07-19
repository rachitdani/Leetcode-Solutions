class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize the variable to count the number of jumps
        res = 0
        # Initialize the pointers l and r to represent the current range of indices
        l,r = 0,0
        # Iterate till the right pointer reaches the last element
        while r < len(nums) - 1:
            # Initialze the farthest jump distance
            farthest = 0
            #Iterate through the indices from l to r
            for i in range(l,r+1):
                #Update the farthest jump distance within the range
                farthest = max(farthest, i + nums[i])
            # Move the left pointer to the end of the current range
            l = r+1
            # Update the right pointer to the farthest distance found
            r = farthest
            # Increment the number of jumps
            res+=1

        # Return the total number of jumps taken to reach last element
        return res


        