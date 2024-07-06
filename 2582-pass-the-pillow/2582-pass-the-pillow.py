class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        curr_position, curr_time= 1,0
        direction = 1
        while curr_time < time:
            if 0 < curr_position + direction <= n:
                curr_position+= direction
                curr_time+=1

            else:
                # Reverse the direction if the next position is out of bounds
                direction*=-1

        return curr_position