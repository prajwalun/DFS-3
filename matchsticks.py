# makesquare:
# - Check if total length is divisible by 4 (each side of square).
# - Sort matchsticks in descending order for efficient pruning.
# - Try placing each stick on 1 of 4 sides using backtracking.
# - Return True if all 4 sides are equal to target length.

# TC: O(4^n), but optimized by sorting and early pruning.
# SC: O(n), for recursion stack and sides array.


from typing import List  

class Solution:  
    def makesquare(self, matchsticks: List[int]) -> bool:  
        total_length = sum(matchsticks)  
        if total_length % 4 != 0:  
            return False  
        side_length = total_length // 4  
        matchsticks.sort(reverse=True)  
        sides = [0] * 4  
        
        def backtrack(index):  
            if index == len(matchsticks):  
                return all(side == side_length for side in sides)  
            for i in range(4):  
                if sides[i] + matchsticks[index] <= side_length:  
                    sides[i] += matchsticks[index]  
                    if backtrack(index + 1):  
                        return True  
                    sides[i] -= matchsticks[index]  
                if sides[i] == 0:  
                    break  
            return False  
        
        return backtrack(0)