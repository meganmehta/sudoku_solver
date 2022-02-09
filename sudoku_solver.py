# Solving the Sudoku Problem - CS 411 Programming Assignment #1 

# Resources: 
# -https://www.geeksforgeeks.org/sudoku-backtracking-7/


#TO-DO: create function to accept input (parse | to form arrays)
#example given in problem definition sheet 
from logging import shutdown
from re import S
from tabnanny import check


sudoku_grid = grid =[
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

#this function will print out the current grid 
def print_grid(sudoku_grid):
    for i in range(9):
        for j in range(9):
            print(sudoku_grid[i][j], end = "|")
        print(" ")

# Sudoku Constraints: 
# - every number must appear ONCE in each row and column 
# - in the subsquare, every number 1-9 must be present 

def check_constraints(sudoku_grid, row, column, value): 
    
    #check if value exists in row already 
    if value in sudoku_grid[row]:
        print(value, "already exists in row ", row)
    
    #check if value exists in the selected column 
    for i in range(9):
        if sudoku_grid[i][column] == value:
            print(value, "already exists in column ", column)
            
    #check if value exists in sub-square 
            
def solve_sudoku(sudoku_grid):
    #iterate through every cell in the grid to make sure that constriants are met 
    

    print("solved")

check_constraints(sudoku_grid, 0, 5, 8) #remember that each row/column starts at zero!!!
