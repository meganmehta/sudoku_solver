# Sudoku Solver 

## Overview of functions 

`check_constraints(sudoku_grid, row, column, value)`

This function contains all of the **consistency checks**: does value exist in row? does value exist in column? does value exist in sub-grid? 
for loops are used to iterate through all parts of the 9x9 matrix, and the function only returns true if each of these 
constraints are true. 

`find_empties(sudoku_grid)`

This function will iterate through the entire sudoku_grid and find any spot that is 0 (ie: hasn't been solved for yet).

`solve_sudoku(sudoku_grid)`

This function utilizes the previous two functions to actually solve the board. `find_empties(sudoku_grid)` is first called 
to get the space that needs to be solved. Then a for loop is used to iterate through the possible values that the space 
could be. If the possible value is a valid (ie: `check_constraints(sudoku_grid, row, column, value)` is true) then it will
set that value in the sudoku_grid matrix. This function is then recursively called, and only **backtracked** if the initial 
value assigned was incorrect. 

`write_output_file(sudoku_grid)`

This function will write the final sudoku_grid to a .txt file. 
