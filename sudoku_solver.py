# Solving the Sudoku Problem - CS 411 Programming Assignment #1 

# Sudoku Constraints: 
# - every number must appear ONCE in each row and column 
# - in the subsquare, every number 1-9 must be present 
import sys 

def check_constraints(sudoku_grid, row, column, value): 
    
    for i in range(9):
        if sudoku_grid[row][i] == value:
            return False
        
    #check if value exists in the selected column 
    for i in range(0, 9):
        if sudoku_grid[i][column] == value:
            #print("in same column")
            return False  
            
    #check if value exists in sub-square 
    #get current row and column position + 3 to establish grid 
    subRow = (row // 3) * 3
    subCol = (column // 3) * 3
    
    for i in range(subRow, subRow + 3):
        for j in range(subCol, subCol + 3):
            if sudoku_grid[i][j] == value:
                return False
            
    return True

#gets the position of what box needs to be solved 
def find_empties(sudoku_grid):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_grid[i][j] == 0:
                return i, j
            
    return None

def solve_sudoku(sudoku_grid):
    to_solve = find_empties(sudoku_grid)
    if to_solve is None:
        return True
    else:
        curRow, curCol = to_solve
    
    #testing possible values, if constraints are met then set it in the grid 
    #then move on to the next empty space 
    for i in range(1, 10):
        if check_constraints(sudoku_grid, curRow, curCol, i):
            sudoku_grid[curRow][curCol] = i 
            if solve_sudoku(sudoku_grid):
                return True
        
            sudoku_grid[curRow][curCol] = 0 #backtrack step 
            
    return False

def write_grid(sudoku_grid):
    for i in range(9):
        for j in range(9):
            print(sudoku_grid[i][j], end = "|")
        print(" ")
                  
if __name__ == '__main__':
    
    '''#accept file input + read file into matrix 
    input_file = input("Enter sudoku .txt file here: ")
    sudoku_grid = [ [ 0 for i in range(9) ] for j in range(9) ]
    countRow = 0
    countCol = 0
    
    with open (input_file, 'r') as f:
        read_data = f.read()
        content_list = read_data.split("\n")
        output = [i for item in content_list for i in item]

    print(output)
    print(sudoku_grid)'''
    
    '''sudoku_grid = [
        [8, 0, 0, 9, 3, 0, 0, 0, 2],
        [0, 0, 9, 0, 0, 0, 0, 4, 0],
        [7, 0, 2, 1, 0, 0, 9, 6, 0],
        [2, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 7, 0, 0, 0, 6, 0, 0, 5], #HAD THE WRONG THING OMG 
        [0, 2, 7, 0, 0, 8, 4, 0, 6],
        [0, 3, 0, 0, 0, 0, 5, 0, 0],
        [5, 0, 0, 0, 6, 2, 0, 0, 8]
    ]'''
    
    sudoku_grid = [
        [0, 0, 0, 6, 0, 0, 4, 0, 0],
        [7, 0, 0, 0, 0, 3, 6, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 1, 8, 0, 0, 0, 3],
        [0, 0, 0, 3, 0, 6, 0, 4, 5],
        [0, 4, 0, 2, 0, 0, 0, 6, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 1, 0, 0]
    ]
    
    if solve_sudoku(sudoku_grid):
        write_grid(sudoku_grid)
    else:
        print("puzzle can't be solved")

