def find_empty_location(grid):
    # Find the next empty cell in the grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def is_valid(grid, row, col, num):
    # Check if it's valid to place 'num' in grid[row][col]
    
    # Check if num is not already in the row
    if num in grid[row]:
        return False
    
    # Check if num is not already in the column
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # Check if num is not already in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve_sudoku(grid):
    # Using backtracking to solve the Sudoku puzzle
    
    # Find the first empty location
    find = find_empty_location(grid)
    if not find:
        return True  # If no empty location is found, puzzle is solved
    
    row, col = find
    
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num  # Place the number if it's valid
            
            if solve_sudoku(grid):
                return True  # Recursively solve the rest of the puzzle
            
            grid[row][col] = 0  # Backtrack if no valid number works
    
    return False  # Trigger backtracking

def print_sudoku(grid):
    # Print the Sudoku grid in a readable format
    for row in grid:
        print(" ".join(map(str, row)))

# Example usage:
if __name__ == "__main__":
    # Example unsolved Sudoku grid
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku Grid:")
    print_sudoku(sudoku_grid)
    print("\nSolving...\n")

    if solve_sudoku(sudoku_grid):
        print("Solved Sudoku Grid:")
        print_sudoku(sudoku_grid)
    else:
        print("No solution exists.")
