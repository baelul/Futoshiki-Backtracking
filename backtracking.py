from objects import *
import random
import copy

domainValues = [1,2,3,4,5]

## Check for constraints left of inequality
def leftConstraints(value, tile, right):
    if tile.constraints['L'] == '<': # needs to be value < right
        if value in tile.legalMoves:
            if right.value != 0:
                if value > right.value:
                    return False
            if value == 5:
                return False
            return True
        return False

    if tile.constraints['L'] == '>': # needs to be value > right
        if value in tile.legalMoves:
            if right.value != 0:
                if value < right.value:
                    return False
            if value == 1:
                return False
            return True
        return False
    
## Check for constraints right of inequality
def rightConstraints(value, tile, left):
    if tile.constraints['R'] == '<': # needs to be left < value
        if value in tile.legalMoves:
            if left.value != 0:
                if left.value > value:
                    return False
            if value == 1:
                return False
            return True
        return False

    if tile.constraints['R'] == '>': # needs to be left > value
        if value in tile.legalMoves:
            if left.value != 0:
                if left.value < value:
                    return False
            if value == 5:
                return False
            return True
        return False

## Check for constraints above the inequality
def topConstraints(value, tile, bottom):
    if tile.constraints['T'] == 'v': # needs to be value > bottom
        if value in tile.legalMoves:
            if bottom.value != 0:
                if value < bottom.value:
                    return False
            if value == 1:
                return False
            return True
        return False

    if tile.constraints['T'] == '^': # needs to be value < bottom
        if value in tile.legalMoves:
            if bottom.value != 0:
                if value > bottom.value:
                    return False
            if value == 5:
                return False
            return True
        return False

## Check for constraints below the inequality
def bottomConstraints(value, tile, top):
    if tile.constraints['B'] == 'v': # needs to be top > value
        if value in tile.legalMoves:
            if top.value != 0:
                if top.value < value:
                    return False
            if value == 5:
                return False
            return True
        return False

    if tile.constraints['B'] == '^': # needs to be top < value
        if value in tile.legalMoves:
            if top.value != 0:
                if top.value > value:
                    return False
            if value == 1:
                return False
            return True
        return False

## Checks for constraint violations
## Returns True or False
def constraintConsistent(value, tile, csp):
    top = True
    bottom = True
    left = True
    right = True

    if 'B' in tile.constraints:
        bottom = bottomConstraints(value, tile, csp.boardDict[(tile.location[0], tile.location[1]-1)])

    if 'T' in tile.constraints:
        top = topConstraints(value, tile, csp.boardDict[(tile.location[0], tile.location[1]+1)])

    if 'R' in tile.constraints:
        right = rightConstraints(value, tile, csp.boardDict[(tile.location[0]-1, tile.location[1])])
            
    if 'L' in tile.constraints:
        left = leftConstraints(value, tile, csp.boardDict[(tile.location[0]+1, tile.location[1])])

    return top and bottom and left and right


## Checks entire column for violations
## Returns True or False
def colConsistent(value, tile, csp):
    col_index = tile.location[0]

    for node in csp:
        if node.location[0] == col_index and node.value == value:
            return False
    return True

## Checks entire row for violations
## Returns True or False   
def rowConsistent(value, tile, csp):
    row_index = tile.location[1]

    for node in csp:
        if node.location[1] == row_index and node.value == value:
            return False
    return True

## Checks row and updates legal moves
def rowCheck(tile, csp):
    row_index = tile.location[1]

    for node in csp:
        if node.location[1] == row_index and node.value in tile.legalMoves:
            tile.legalMoves.remove(node.value)

## Checks col and updates legal moves
def colCheck(tile, csp):
    col_index = tile.location[0]

    for node in csp:
        if node.location[0] == col_index and node.value in tile.legalMoves:
            tile.legalMoves.remove(node.value)

# Updates legal moves 
def determineLegalMoves(tile, csp):
    tile.legalMoves = [1,2,3,4,5]
    rowCheck(tile, csp)
    colCheck(tile, csp)

## Evaluates if a possible value definition is valid (doesnt violate constraints)
## Returns True or False
def isConsistent(value, tile, csp, assignment):
    if len(t.legalMoves) == 0:
        return False
    return colConsistent(value, tile, assignment) and rowConsistent(value, tile, assignment) and constraintConsistent(value, tile, csp)

## Select Unassigned Variable (MRV and Degree)
## Returns Tile object selected
def selectUnassignedVariable(csp, assignment):
    # Minimum Remaining Value
    legalMovesLeftList = []
    for t1 in csp.state:
        determineLegalMoves(t1, assignment)
        if t1.value == 0:
            legalMovesLeftList.append([t1,len(t1.legalMoves)])
    legalMovesLeftList.sort(key=lambda x:x[1])

    if len(legalMovesLeftList) == 1 or legalMovesLeftList[0][1] != legalMovesLeftList[1][1]:
        return legalMovesLeftList[0][0]
    else:
        # Degree
        mostConstraintsList = []
        for t2 in csp.state:
            if t2.value == 0:
                mostConstraintsList.append([t2,len(t2.constraints)])
        mostConstraintsList.sort(reverse=True,key=lambda x:x[1])
        if mostConstraintsList[0][1] != mostConstraintsList[1][1]:
            return mostConstraintsList[0][0]

    # Degree doesn't work (arbitrarily choose)
    rand_input = random.randrange(len(legalMovesLeftList))
    return legalMovesLeftList[rand_input][0]

## Backtracking Search Algorithm
def backtrackingSearch(csp):
    # call actual algorithm
    assignment = {}
    for tile in csp.state:
        if tile.value != 0:
            assignment[tile] = tile.value
    return backtrack(csp, assignment)
    
## Algorithm Implementation
def backtrack(csp, assignment):
    if len(assignment) == 25:
        return csp
    tile = selectUnassignedVariable(csp, assignment) # tile object
    for value in domainValues:
        if isConsistent(value, tile, csp, assignment):
            # add {var = value} to assignment
            assignment[tile] = value
            oldMoves = copy.deepcopy(tile.legalMoves)
            tile.value = value

            result = backtrack(csp, assignment)

            if result != "FAILURE":
                return result

            # remove {var = value} to assignment
            del assignment[tile]
            tile.value = 0
            tile.legalMoves = oldMoves

    return "FAILURE" # fail           
