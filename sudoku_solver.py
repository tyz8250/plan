def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def format_sudoku_string(sudoku_string):
    formatted_lines = []
    lines = sudoku_string.strip().split("\n")
    for line in lines:
        formatted_line = ' '.join(line[i] for i in range(9))
        formatted_lines.append(formatted_line)
    return '\n'.join(formatted_lines)

def string_to_board(sudoku_string):
    board = []
    rows = sudoku_string.strip().split("\n")
    for row in rows:
        board.append([int(num) if num != '.' else 0 for num in row.split()])
    return board

# 数独ボードを9桁の数字形式で入力
sudoku_string = """
530070000
600195000
098000060
800060003
400803001
700020006
060000280
000419005
000080079
"""

formatted_sudoku_string = format_sudoku_string(sudoku_string)
board = string_to_board(formatted_sudoku_string)

print("Unsolved Sudoku:")
print_board(board)
solve(board)
print("\nSolved Sudoku:")
print_board(board)
