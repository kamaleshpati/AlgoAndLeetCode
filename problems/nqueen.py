class NQueen:
    def solveNQueens(self, n: int) -> list[list[str]]:
        if n == 1:
            return [["Q"]]
        else:
            board = [["." for i in range(0,n)] for j in range(0,n)]

            if self.placeNQueen(board, 0, n):
                return board

    def placeNQueen(self, board, col, n):
        if col >= n:
            return True
        else:
            for i in range(n):
                if self.isSafe(board, i, col, n):
                    board[i][col] = "Q"
                    if self.placeNQueen(board, col+1, n):
                        return True
                    board[i][col] = "."
            return False

    def isSafe(self, board, row, col, N):

        # Check this row on left side
        for i in range(col):
            if board[row][i] == "Q":
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, N, 1),
                        range(col, -1, -1)):
            if board[i][j] == "Q":
                return False

        return True


if __name__ == '__main__':
    print(NQueen().solveNQueens(4))

