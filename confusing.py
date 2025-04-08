# confusingNumberII:
# - Generate numbers using only rotatable digits (0,1,6,8,9).
# - Use DFS to build numbers ≤ N, skipping invalid leading zeros.
# - For each number, check if its rotation differs (confusing).
# - Count all such valid confusing numbers.

# TC: O(logN) per number, overall bounded by DFS tree size (~10^5).
# SC: O(logN) for recursion stack during DFS.


class Solution:
    def confusingNumberII(self, N: int) -> int:
        rotatables = [1, 0, 6, 8, 9]
        rotation_map = {1:1, 0:0, 6:9, 8:8, 9:6}        
        confusing_number_count = 0
        
        def count_rotatables(cur_num=0):
            nonlocal confusing_number_count
            if cur_num * 10 > N:
                return
            for num in rotatables:
                next_num = cur_num*10 + num
                if next_num == 0:
                    continue
                confusing_number_count += next_num <= N and is_valid_rotation(next_num)
                count_rotatables(next_num)
        
        def is_valid_rotation(num):
            rotated = 0
            cur_num = num
            while cur_num:
                rotated = rotated * 10 + rotation_map[cur_num%10]
                cur_num //= 10
            return rotated != num
        
        count_rotatables()
        
        return confusing_number_count