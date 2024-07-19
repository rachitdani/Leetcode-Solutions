class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for elem in nums:
            if start < 0:
                return False
            elif elem > start:
                start = elem
            start -=1
        
        return True
            
            
        