# Solving the Sudoku Problem - CS 411 Programming Assignment #1 

# Resources: 
# -https://www.geeksforgeeks.org/sudoku-backtracking-7/
# -https://dev.to/christinamcmahon/use-backtracking-algorithm-to-solve-sudoku-270 

# Sudoku Constraints: 
# - every number must appear ONCE in each row and column 
# - in the subsquare, every number 1-9 must be present 

def check_constraints(sudoku_grid, row, column, value): 
    count = 0
    
    #check if value exists in the selected column 
    for i in range(0, 9):
        if sudoku_grid[i][column] == value:
            #print("in same column")
            return False  
            
    #check if value exists in sub-square 
    #get current row and column position + 3 to establish grid 
    subRow = int(row - row%3)
    subCol = int(column - column%3)
    
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_grid[i + subRow][j + subCol] == value:
                #print("in sub")
                return False
               
    #check if value exists in row already 
    if value in sudoku_grid[row]:
        #print("in same row")
        return False
    else: 
        return True

#gets the position of what box needs to be solved 
def find_empties(sudoku_grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_grid[i][j] == 0:
                return i, j
    return -1 

def solve_sudoku(sudoku_grid):
    to_solve = find_empties(sudoku_grid)
    if not to_solve:
        print("no empties")
        return True
    else:
        curRow, curCol = to_solve

    print(curRow, ", ", curCol)
    
    for i in range(1, 10):
        if check_constraints(sudoku_grid, curRow, curCol, i) is True:
            sudoku_grid[curRow][curCol] = i 
            if solve_sudoku(sudoku_grid):
                print("got it")
                return True
            sudoku_grid[curRow][curCol] = 0 #backtrack step 
           
    return False

def print_grid(sudoku_grid):
    for i in range(9):
        for j in range(9):
            print(sudoku_grid[i][j], end = "|")
        print(" ")
                  
def main():
    
    sudoku_grid = [
        [8, 0, 0, 9, 3, 0, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 0, 4, 0],
        [7, 0, 2, 1, 0, 0, 9, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 0, 5],
        [0, 7, 0, 0, 0, 6, 0, 0, 5],
        [0, 2, 7, 0, 0, 8, 4, 0, 6],
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 2, 0, 0, 8]
    ]
    solve_sudoku(sudoku_grid)
    #find_empties(sudoku_grid)
    print_grid(sudoku_grid)

main()