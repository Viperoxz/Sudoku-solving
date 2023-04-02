from pprint import pprint

def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None #if no space in puzzle is empty

def is_valid(puzzle, guess, row, col):
    #check if the guess is valid by row, column and 3x3 square
    #row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    #column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    #square
    row_start = (row // 3)*3
    col_start = (col // 3)*3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    return True

def sudoku_solve(puzzle):
    # 1. Find somewhere on the puzzle to start
    row, col = find_next_empty(puzzle)
    # 1.1. if there's no where left, then we're done
    if row is None:
        return True
    # 2. if there still a place to put a number, make a guess between 1-9
    for guess in range(1,10):
        # 3. check if this is valid guess
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            # 4. Recursively call our function
            if sudoku_solve(puzzle):
                return True
        puzzle[row][col] = -1 # reset the guess if it's not the answer

    # 5. if none of the numbers we try work, this puzzle is UNSOLVABLE
    return False

# Test
if __name__=='__main__':

    board = [
        [-1, 6, 4,  -1, -1, -1,   -1, -1, -1],
        [2, -1, -1,   -1, -1, 9,   -1, -1, 3],
        [-1, 9, -1,   -1, 4, -1,   -1, -1, 5],

        [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [8, -1, -1,   -1, -1, 2,   -1, -1, 1],
        [9, -1, -1,   7, -1, -1,   -1, 5, -1],

        [6, -1, 8,   -1, 2, -1,   -1, 7, -1],
        [5, -1, -1,   -1, -1, 1,   -1, 8, -1],
        [-1, -1, -1,   -1, -1, 4,   -1, 6, -1]
        ]


    print(sudoku_solve(board))
    pprint(board)
