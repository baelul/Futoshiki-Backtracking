from backtracking import *
from objects import *

## Read Input File
def readInputFile(filename):
    initial_state = []
    
    # ineqs are the lines of the grid between the values
    hor_ineqs = [] # > or <
    ver_ineqs = [] # ^ or v
    input_file = open(filename)

    line_count = 0
    # read and handle each line of input
    for line in input_file:
        # if line ISN'T empty, handle
        if line != "\n":
            # determines where to store lines
            if line_count >= 0 and line_count <= 4:  # initial
                initial_state.append(line.split())
            elif line_count >= 6 and line_count <= 10: # horizontal
                hor_ineqs.append(line.split())
            elif line_count >= 12 and line_count <= 15: # vertical
                ver_ineqs.append(line.split())
        line_count += 1
    input_file.close() # must close file!
    return initial_state, hor_ineqs, ver_ineqs

## Create Output File
def createOutputFile(solution, file_num):
    filename = "Output" + str(file_num) + ".txt"
    output_file = open(filename, 'w')

    if solution != "FAILURE":
        x = 0
        for tile in solution.state:
            output_file.write(' '.join(str(tile.value)))
            output_file.write(' ')
            x+=1            
            if x % 5 == 0:
                output_file.write("\n")
    else:
        output_file.write(solution)

    output_file.close() # must close file!

## MAIN FUNC
def main():
    filename = input("Enter name of file: ")
    initial_state, hor_ineqs, ver_ineqs = readInputFile(filename)

    csp = Board(initial_state, [], hor_ineqs, ver_ineqs)
    solution = backtrackingSearch(csp)

    file_num = filename[5] # number from input filename
    createOutputFile(solution, file_num)

## Call main()
main()
    
