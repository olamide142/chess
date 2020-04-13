from board import Board
from movement import *
import time




class Piece(Board):
    piece = None
    position = None
    previousPosition = None
    previousPiece = None
    futurePosition = None 
    youDoIt = True

    def __init__(self, pos, piece):
        # This is probably not a correct way to 
        # do this... 
        Piece.piece = piece
        Piece.position = pos
        Piece


    def __str__(self):
        return f"{self.position} : {self.piece}"
        

    def change(self, piece, currentPos, futurePosition):
        self.check = validateMove(p, currentPos, futurePosition)

    
    def validateMove(future_piece, previous_position, future_position, previous_piece):
        """
        future_piece: the name of the piece or 'empty' to capture
        previous_position: the position of the attacking piece
        future_position: the location of future_piece 
        previous_piece: the name of the attacking piece
        """
        
        # Get the array index of previous_position and future_position
        # fnctions are in movement.py
        currentPosition = getIndexOfPosition(previous_position)
        destinationPosition = getIndexOfPosition(future_position)

        # Check that player is not attacking himself
        if Board.play_belongs_to in future_piece:
            print("You cant attack yourself")
            print(f"Current Player: {Board.play_belongs_to}, Future Piece: {future_piece}")

            return False

        # check if it is the current players turn
        if ( (('white' in Board.play_belongs_to) and ('white' in previous_piece)) or (('black' in Board.play_belongs_to) and ('black' in previous_piece)) ):
            
                # Validate move if attacker is a Rook
                if 'Rook' in previous_piece:
                    return rook(currentPosition, destinationPosition)
                # Validate move if attacker is a Pawn
                elif 'Pawn' in previous_piece:
                    return pawn(currentPosition, destinationPosition)
                # Validate move if attacker is a Bishop
                elif 'Bishop' in previous_piece:
                    return bishop(currentPosition, destinationPosition)
                # Validate move if attacker is a Knight
                elif 'Knight' in previous_piece:
                    return knight(currentPosition, destinationPosition)
                # Validate move if attacker is a Queen
                elif 'Queen' in previous_piece:
                    return queen(currentPosition, destinationPosition)

               
        else:
            print("Wait for your turn")
            print(f"Current Player: {Board.play_belongs_to}")
            return False


            

    def isCapture(p, futurePosition):
        """To check if the future position has a value """
        """if so capture is True"""
        """
        p: name of piece (eg: whiteRook)
        futurePosition: name of future position (eg: A1)
        """
        # print("Currently in is capture")
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
                Piece.position = loc 
                Piece.piece = Board.pieces[loc] 
                # if the player selects the same location
                # twice make position None (De-select piece)
                if Piece.previousPosition is loc:
                    print(f"Selected the same thing Loc:{loc}, Piece.position:{Piece.position}")
                    Piece.position = loc 
                    Piece.piece = Board.pieces[loc]  
                elif (Piece.previousPosition is not None) and (Piece.previousPosition is not Piece.position):
                    # Validate move before changing position to the 
                    # new selected position, Piece.piece, Piece.location 
                    # changes to None to allow a new piece to be selected by 
                    # next player. The list of captured increases for current player

                    # Break this down into at least 2 functions 
                    print(f"PIECE: {Piece.piece}, PREVIOUS POSITION: {Piece.previousPosition}, FUTURE POSITION: {Piece.position}, PREVIOUS PIECE: {Piece.previousPiece}")
                    if Piece.validateMove(Piece.piece, Piece.previousPosition, Piece.position, Piece.previousPiece):
                        if Piece.isCapture(Piece.piece, Board.pieces[loc]):
                            # appendToListOfCaptured(Board.pieces[Piece.position] )
                            # set the piece into new location 
                            if Piece.youDoIt == True:
                                # this will only run if the switch
                                # did not hapen from the movement 
                                # did not already happen at the movementmodule
                                Board.pieces[Piece.position] = Board.pieces[str(Piece.previousPosition)]
                            # change previousPosition location to empty
                            Board.pieces[Piece.previousPosition] = 'empty'
                            Piece.position = None
                            Piece.piece = None 
                            Piece.previousPosition = None
                            Piece.previousPiece = None

                            # Change Player 
                            Board.switch_player()



                    else:
                        '''Return error msg if current player is making a wrong move'''
                        print("You cant make this move")
                        Piece.position = None
                        Piece.piece = None 
                        Piece.previousPosition = None
                        Piece.previousPiece = None
                        break
                        return None #i doubt this line runs

                elif Board.pieces[loc] == 'empty':
                    return None
                else:
                    Piece.previousPosition = loc
                    Piece.previousPiece = Board.pieces[loc]
                    print(f">>>>>>{Piece.previousPiece}")
                    # Board.pieces[loc] = "empty"
                    # print(Piece.previousPosition)
                 
                    return Piece(loc, Board.pieces[loc])
            else:
                pass
