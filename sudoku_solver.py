# Solving the Sudoku Problem - CS 411 Programming Assignment #1 

# Sudoku Constraints: 
# - every number must appear ONCE in each row and column 
# - in the subsquare, every number 1-9 must be present 
import sys

from nbformat import read 

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

def write_output_file(sudoku_grid): 
    #writes solution to new text file 
    with open('solution.txt', 'w') as f:
        for i in sudoku_grid:
            f.write('|' + '|'.join([str(a) for a in i]) + '|\n')
                  
if __name__ == '__main__':
    #accept file input + read file into matrix 
    input_file = input("Enter sudoku .txt file here: ")
    sudoku_grid = []
    
    #reads in text file and parses so that we have a matrix to work with 
    with open (input_file, 'r') as f:
        read_data = f.read()
        content_list = read_data.split("\n")
        row = []
        
        for j in range(0, len(content_list)):
            output = content_list[j]
            row = []
            for i in range(1, len(output)):
                if output[i].isdigit():
                    row.append(int(output[i]))
                elif output[i] == '|' and output[i-1] == '|':
                    row.append(0)
            sudoku_grid.append(row)       
    
    if solve_sudoku(sudoku_grid):
        write_output_file(sudoku_grid)
        print("Puzzle solved successfully! : )")
    else:
        print("Puzzle can't be solved : (")

