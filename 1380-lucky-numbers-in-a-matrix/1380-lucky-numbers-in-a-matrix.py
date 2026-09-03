class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        for i in range(len(matrix)):
            row_min = min(matrix[i])

            col = matrix[i].index(row_min)

            if row_min == max(matrix[r][col] for r in range(len(matrix))):
                ans.append(row_min)

        return ans