from board import Board
import movement
import time




class Piece(Board):
    piece = None
    position = None
    futurePosition = None 

    def __init__(self, pos, piece):
        # This is probably not a correct way to 
        # do this... 
        Piece.piece = piece
        Piece.position = pos


    def __str__(self):
        return f"{self.position} : {self.piece}"
        

    def change(self, piece, currentPos, futurePosition):
        self.check = validateMove(p, currentPos, futurePosition)

    
    def validateMove(p, currentPos, futurePosition):
        """
        p: the name of the piece
        currentPos: the current position of p
        futurePosition: the intended location p is to be moved to
        """
        print("Currently in is validate")
        return True
        # pass
            

    def isCapture(p, futurePosition):
        """To check if the future position has a value """
        """if so capture is True"""
        """
        p: name of piece (eg: whiteRook)
        futurePosition: name of future position (eg: A1)
        """
        print("Currently in is capture")
        return True

        # pass


    def getLocation(x_y):
        locations = Board.locations
        for loc in locations:
            # get the x and y axis of each location 
            # and store it in a x_axis, y_axis tuple 
            x_axis = (locations[loc][0], locations[loc][2])
            y_axis = (locations[loc][1], locations[loc][3])
            # print(f"X axis: {x_axis}, Y axis: {y_axis}")
            # time.sleep(2)
            if (x_y[0] >= x_axis[0] and x_y[0] <= x_axis[1]) and (x_y[1] >= y_axis[0] and x_y[1] <= y_axis[1]):
                # if the player slecets the same location
                # twice make position None (De-select piece)
                if Piece.position is loc:
                    Piece.position = None 
                    Piece.piece = None 
                elif Piece.position is not None:
                    # Validate move before changing position to the 
                    # new selected position, Piece.piece, Piece.location 
                    # changes to None to allow a new piece to be selected by 
                    # next player. The list of captured increases for current player

                    # Break this down into at least 2 functions 
                    if Piece.validateMove(Piece.piece, Piece.position, Board.pieces[loc]):
                        if Piece.isCapture(Piece.piece, Board.pieces[loc]):
                            print("in here")
                            # appendToListOfCaptured(Board.pieces[Piece.position] )
                            # set the piece into new location 
                            Board.pieces[loc] = Piece.piece
                            # change previous location to empty
                            Board.pieces[Piece.position] = 'empty'
                            Piece.position = None
                            Piece.piece = None 
                            Piece.futurePosition = None 

                    else:
                        return "error"
                else: 
                    return Piece(loc, Board.pieces[loc])
