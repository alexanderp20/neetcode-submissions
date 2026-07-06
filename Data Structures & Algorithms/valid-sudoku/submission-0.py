class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            row_dict = {}
            for col in range(len(board[row])):
                if board[row][col] != '.':
                    row_dict[int(board[row][col])] = row_dict.get(int(board[row][col]), 0) + 1
                    if row_dict[int(board[row][col])] > 1:
                        return False
            
        for col in range(len(board)):
            col_dict = {}
            for row in range(len(board[col])):
                if board[row][col] != '.':
                    col_dict[int(board[row][col])] = col_dict.get(int(board[row][col]), 0) + 1
                    if col_dict[int(board[row][col])] > 1:
                        return False
        
        for row in range(0, len(board), 3):
            for col in range(0, len(board), 3):
                matrix_dict = {}
                for i in range(3):
                    for j in range(3):
                        if board[row+i][col+j] != '.':
                            matrix_dict[int(board[row+i][col+j])] = matrix_dict.get(int(board[row+i][col+j]), 0) + 1
                            if matrix_dict[int(board[row+i][col+j])] > 1:
                                return False
        
        return True
