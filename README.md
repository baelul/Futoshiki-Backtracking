# Futoshiki with Backtracking Algorithm
## Project Description
The goal of this project is to implement the Backtracking Algorithm of CSPs to solve 5 x 5 Futoshiki puzzles. Futoshiki is similar to Sudoku, in which a number must be unique in it's own row and column. However, Futoshiki adds inequalities to the board, in which the numbers must adhere to.
## Code Description
There are three files:  
`backtracking.py` which contains the implementation of the backtracking algorithm, as well as any helper functions needed to properly implement it.  
`objects.py` which contains the Tile and Board classes, used in the algorithm.  
`main.py` which contains file I/O and runs the algorithm on a given CSP.  
## How to Run
To run the source code, make sure that all files (main.py, backtracking.py, objects.py) are within the same directory. Open the console/terminal, and change directories to the one containing the files. Any input files must also be in the same directory. Input files must also be named with the following format: Input#.txt, with # being a number from 0-9.  
  
Python must be installed on your computer in order to run the main.py
file. The program runs on 3.11.0, but any version of Python should run
the code.  

Run the following command in the terminal:
`python3 main.py` (if using Python ver. older than 3.0, remove the 3 from this command)  

You will be prompted to enter an input file name. Enter Input#.txt, with # being the number of the input file. Output#.txt will be generated.
