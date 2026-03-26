class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_sum = 0
        smallest_abs = float('inf')
        neg_count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                value = matrix[i][j]

                abs_value = abs(value)
                abs_sum += abs_value

                if value < 0:
                    neg_count += 1

                if abs_value < smallest_abs:
                    smallest_abs = abs_value

       
        if neg_count & 1:
            abs_sum -= 2 * smallest_abs

        return abs_sum
