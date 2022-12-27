# Node class for the board
class Tile:
    def __init__ (self, location = (0,0), value=0, legalMoves = None, constraints = None):
        self.location = location
        self.value = value
        self.legalMoves = [1,2,3,4,5]
        self.constraints = {}

## Board class that holds 25 Tile nodes. Used for CSP
class Board:
    def __init__(self, initial_state, state=[], hor_ineqs=[], ver_ineqs=[]):
        self.state = state
        self.hor_ineqs = hor_ineqs
        self.ver_ineqs = ver_ineqs

        self.fillBoard(initial_state)

        self.row1 = self.state[0 : 5]
        self.row2 = self.state[5 : 10]
        self.row3 = self.state[10 : 15]
        self.row4 = self.state[15 : 20]
        self.row5 = self.state[20 : 25]   

        self.col1 = [self.state[0], self.state[5], self.state[10], self.state[15], self.state[20]]
        self.col2 = [self.state[1], self.state[6], self.state[11], self.state[16], self.state[21]]
        self.col3 = [self.state[2], self.state[7], self.state[12], self.state[17], self.state[22]]
        self.col4 = [self.state[3], self.state[8], self.state[13], self.state[18], self.state[23]]
        self.col5 = [self.state[4], self.state[9], self.state[14], self.state[19], self.state[24]]

        self.evalConstraints()   

        self.boardDict = {} 

        for tile in self.state:
            self.boardDict[tile.location] = tile

    ## Creates 25 tiles objects, if a state in given, the board will be filled with the values from that input
    def fillBoard(self, input_board):  
        for y in range(5):
            for x in range(5):
                tile = Tile((x,y))
                if input_board != None:
                    tile.value = int(input_board[y][x])
                self.state.append(tile)

    ## Call evalHorizontalConstraints() and evalVerticalConstraints()
    def evalConstraints(self):
        self.evalHorizontalConstraints()
        self.evalVerticalConstraints()

    ## Add horizontal constraints to each tile in the Board
    def evalHorizontalConstraints(self):
        hLine1 = self.hor_ineqs[0]
        hLine2 = self.hor_ineqs[1]
        hLine3 = self.hor_ineqs[2]
        hLine4 = self.hor_ineqs[3]
        hLine5 = self.hor_ineqs[4]

        for i in range(len(hLine1)): # len of all lines is same
            if hLine1[i] in "><":
                self.row1[i].constraints["L"] = hLine1[i]
                self.row1[i+1].constraints["R"] = hLine1[i]                   
                
            if hLine2[i] in "><":
                self.row2[i].constraints["L"] = hLine2[i]
                self.row2[i+1].constraints["R"] = hLine2[i]

            if hLine3[i] in "><":
                self.row3[i].constraints["L"] = hLine3[i]
                self.row3[i+1].constraints["R"] = hLine3[i]

            if hLine4[i] in "><":
                self.row4[i].constraints["L"] = hLine4[i]
                self.row4[i+1].constraints["R"] = hLine4[i]

            if hLine5[i] in "><":
                self.row5[i].constraints["L"] = hLine5[i]
                self.row5[i+1].constraints["R"] = hLine5[i]
                
    ## Add vertical constraints to each tile in the Board
    def evalVerticalConstraints(self):
        vLine1 = self.ver_ineqs[0]
        vLine2 = self.ver_ineqs[1]
        vLine3 = self.ver_ineqs[2]
        vLine4 = self.ver_ineqs[3]

        for i in range(len(vLine1)): # len of all lines is same
            if vLine1[i] in "^v":
                self.row1[i].constraints["T"] = vLine1[i]
                self.row2[i].constraints["B"] = vLine1[i]
            
            if vLine2[i] in "^v":
                self.row2[i].constraints["T"] = vLine2[i]
                self.row3[i].constraints["B"] = vLine2[i]

            if vLine3[i] in "^v":
                self.row3[i].constraints["T"] = vLine3[i]
                self.row4[i].constraints["B"] = vLine3[i]

            if vLine4[i] in "^v":
                self.row4[i].constraints["T"] = vLine4[i]
                self.row5[i].constraints["B"] = vLine4[i]