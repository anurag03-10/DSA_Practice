#https://leetcode.com/problems/set-matrix-zeroes/submissions/1905902291/

class Solution(object):
    def setZeroes(self, matrix):
        rows = set()
        cols = set()

        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j] = 0
