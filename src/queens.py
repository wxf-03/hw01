def solve_n_queens(n):
    result = []
    board = ['.' * n for _ in range(n)]

    def backtrack(row, cols, diag1, diag2, path):
        if row == n:
            result.append(path.copy())
            return
        for col in range(n):
            d1 = row - col
            d2 = row + col
            if col not in cols and d1 not in diag1 and d2 not in diag2:
                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                path.append(board[row][:col] + 'Q' + board[row][col+1:])
                backtrack(row + 1, cols, diag1, diag2, path)
                path.pop()
                diag2.remove(d2)
                diag1.remove(d1)
                cols.remove(col)

    backtrack(0, set(), set(), set(), [])
    return result
