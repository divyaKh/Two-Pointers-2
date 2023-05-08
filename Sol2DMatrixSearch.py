"""
LC 240. Search a 2D Matrix II

TC = O(N*M) and SC = O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r, c = 0, n-1
        while 0<=r<m and 0<=c<n:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target: #move left
                c -= 1
            elif matrix[r][c] < target: #move down
                r += 1
        return False