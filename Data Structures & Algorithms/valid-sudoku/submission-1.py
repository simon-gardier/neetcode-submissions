class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                else:
                    cell = int(board[i][j])
                    if cell in rows[i] or cell in col[j] or cell in squares[(3 * (i // 3)) + (j // 3)]:
                        return False
                    else:
                        rows[i].add(cell)
                        col[j].add(cell)
                        squares[(3 * (i // 3)) + (j // 3)].add(cell)

        # O(N^2)
        return True
