class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                break
            # if (middle > 0 and matrix[middle-1][-1] < target < matrix[middle][0]) or (matrix[middle][-1] < target < matrix[middle+1][0]):
            #     return False
            if target < matrix[middle][0]:
                right = middle - 1
            elif target > matrix[middle][-1]:
                left = middle + 1

        if not(matrix[middle][0] <= target <= matrix[middle][-1]):
            return False

        line = middle
        left = 0
        right = len(matrix[line]) - 1

        while left <= right:
            middle = (left + right) // 2
            if matrix[line][middle] == target:
                return True
            if target < matrix[line][middle]:
                right = middle - 1
            elif target > matrix[line][middle]:
                left = middle + 1

        return target == matrix[line][middle]
