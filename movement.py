from board import Board
import piece
class Movement(Board):
    boardArr = [
        ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
        ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
        ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
        ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
        ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
        ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
        ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
        ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
    ]
    A_copy = Board.pieces



# Parse the status of Board.pieces into a 8x8 Array
def parseBoardToArray():
    x = 0
    y = 0
    for i in Movement.pieces:
        if 'black' in Board.pieces[i]:
            Movement.boardArr[x][y] = 'black'
        elif 'white' in Board.pieces[i]:
            Movement.boardArr[x][y] = 'white'
        else:
            Movement.boardArr[x][y] = 'empty'

        y += 1
        if y > 7:
            y = 0
            x+=1
    # return None


def getIndexOfPosition(position):
    """Returns the inedex of given position"""
    # This is not a good approach 
    # but it gets the job done
    x = 0
    y = 0
    for i in Movement.A_copy:
        if i == position:
            return (x,y)
        y += 1
        if y > 7:
            y = 0
            x+=1


def isPositionValidInArray(position):
    """Returns True if such index exists in the array"""
    # This is not a good approach 
    # but it gets the job done
    x = 0
    y = 0
    for i in Movement.A_copy:
        if (x,y) == position:
            return True
        y += 1
        if y > 7:
            y = 0
            x+=1
    return False





# TYPES OF PIECE





def rook(currentPosition, destinationPosition):
    # list of positions that can be played to 
    VALID_LIST = []

    parseBoardToArray()
    """Check if this move is valid for a Rook"""

    active = True

    left = True
    top = True
    right = True
    bottom = True 

    while active:
        x,y = currentPosition
        # Check all the boxes to the left of current position
        # and stops when there is a filled box
        while left:
            y -=1
            if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # Check if the position is not empty
                if Movement.boardArr[x][y] != 'empty':
                    # check if the piece occupying it is players piece
                    # if so stop checkin this direction
                    if Movement.boardArr[x][y] == Board.play_belongs_to:
                        left = False
                    else:
                        # if this postion is occupied by opponnet piece
                        # this position is valid but every other position 
                        # after it is invalid  
                        VALID_LIST.append((x,y))
                        left = False
                elif Movement.boardArr[x][y] == Board.play_belongs_to:
                    left = False
                else:
                    VALID_LIST.append((x,y))

            else:
                left = False
        x,y = currentPosition
            



        # Check all the boxes to the top of current position
        # and stops when there is a filled box
        while top:
            x -=1
            if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # Check if the position is not empty
                if Movement.boardArr[x][y] != 'empty':
                    # check if the piece occupying it is players piece
                    # if so stop checkin this direction
                    if Movement.boardArr[x][y] == Board.play_belongs_to:
                        top = False
                    else:
                        # if this postion is occupied by opponnet piece
                        # this position is valid but every other position 
                        # after it is invalid  
                        VALID_LIST.append((x,y))
                        top = False
                elif Movement.boardArr[x][y] == Board.play_belongs_to:
                    top = False
                else:
                    VALID_LIST.append((x,y))

            else:
                top = False
        x,y = currentPosition
            

        
        # Check all the boxes to the right of current position
        # and stops when there is a filled box
        while right:
            y +=1
            if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # Check if the position is not empty
                if Movement.boardArr[x][y] != 'empty':
                    # check if the piece occupying it is players piece
                    # if so stop checkin this direction
                    if Movement.boardArr[x][y] == Board.play_belongs_to:
                        right = False
                    else:
                        # if this postion is occupied by opponnet piece
                        # this position is valid but every other position 
                        # after it is invalid  
                        VALID_LIST.append((x,y))
                        right = False
                elif Movement.boardArr[x][y] == Board.play_belongs_to:
                    right = False
                else:
                    VALID_LIST.append((x,y))

            else:
                right = False
        x,y = currentPosition



        # Check all the boxes to the bottom of current position
        # and stops when there is a filled box
        while bottom:
            x +=1
            if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # Check if the position is not empty
                if Movement.boardArr[x][y] != 'empty':
                    # check if the piece occupying it is players piece
                    # if so stop checkin this direction
                    if Movement.boardArr[x][y] == Board.play_belongs_to:
                        bottom = False
                    else:
                        # if this postion is occupied by opponnet piece
                        # this position is valid but every other position 
                        # after it is invalid  
                        VALID_LIST.append((x,y))
                        bottom = False
                elif Movement.boardArr[x][y] == Board.play_belongs_to:
                    bottom = False
                else:
                    VALID_LIST.append((x,y))

            else:
                bottom = False
        x,y = currentPosition


        # Stop The main loop
        active = False
        print(f"\n\n Valid LIST : {VALID_LIST}")
        if destinationPosition in VALID_LIST:
            return True
        else:
            return False




def pawn(currentPosition, destinationPosition):
     # list of positions that can be played to 
    VALID_LIST = set([])

    parseBoardToArray()
    """Check if this move is valid for a Rook"""

    active = True

    while active:

        x,y = currentPosition


        # Check diagonalTopRight 
        x = x-1
        y = y+1
        if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # if this position is not empty
                # and the players own piece is 
                # not the occupant. VALID
                if (Movement.boardArr[x][y] != 'empty') and (Board.play_belongs_to not in Movement.boardArr[x][y]):
                    VALID_LIST.add((x,y))
                else:
                    pass 
                    # Do Nothing
        else:
            pass
            # Do Nothing
        x,y = currentPosition
        


        # Check the diagonalTopLeft
        x = x-1
        y = y-1
        if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # if this position is not empty
                # and the players own piece is 
                # not the occupant. VALID
                if (Movement.boardArr[x][y] != 'empty') and (Board.play_belongs_to not in Movement.boardArr[x][y]):
                    VALID_LIST.add((x,y))
                else:
                    pass 
                    # Do Nothing
        else:
            pass
            # Do Nothing
        x,y = currentPosition



        # check diagonalBottomRight
        x = x+1
        y = y+1
        if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # if this position is not empty
                # and the players own piece is 
                # not the occupant. VALID
                if (Movement.boardArr[x][y] != 'empty') and (Board.play_belongs_to not in Movement.boardArr[x][y]):
                    VALID_LIST.add((x,y))
                else:
                    pass 
                    # Do Nothing
        else:
            pass
            # Do Nothing
        x,y = currentPosition



        # check diagoanlBottomLeft
        x = x+1
        y = y-1
        if isPositionValidInArray((x, y)):
                parseBoardToArray()
                # if this position is not empty
                # and the players own piece is 
                # not the occupant. VALID
                if (Movement.boardArr[x][y] != 'empty') and (Board.play_belongs_to not in Movement.boardArr[x][y]):
                    VALID_LIST.add((x,y))
                else:
                    pass 
                    # Do Nothing
        else:
            pass
            # Do Nothing
        x,y = currentPosition




        # check forward movement 
        # check if pawn is at initial position
        # if so pawn is vid to move 2 steps forward


        # CHECK FOR WHITE ROOK 
        from piece import Piece
        if (x == 6) and (Movement.boardArr[x][y] in Piece.previousPiece) and (Movement.boardArr[x][y] == 'white'):
    
            # 2 steps forward valid 
            parseBoardToArray()
            x = x-1
            if (Movement.boardArr[x][y] == 'empty') or (Movement.boardArr[x][y] == Board.opposite(Board.play_belongs_to)):
                VALID_LIST.add((x,y))
                # Check the next step forward
                x = x-1
                if (Movement.boardArr[x][y] == 'empty') and (Movement.boardArr[x+1][y] == 'empty') or (Movement.boardArr[x][y] == Board.opposite(Board.play_belongs_to)):
                    if isPositionValidInArray((x, y)):
                        VALID_LIST.add((x,y))
            else:
                pass
            x,y = currentPosition


        elif (x != 6) and (Piece.previousPiece == 'whitePawn'):
            # 2 steps forward invalid only one 
            x = x-1
            if (Movement.boardArr[x][y] == 'empty') or (Movement.boardArr[x][y] == Board.opposite(Board.play_belongs_to)):
                print("{+}Everthimg is a it back to back")
                if isPositionValidInArray((x, y)):
                    VALID_LIST.add((x,y))
            else:
                pass
            x,y = currentPosition


        # CHECK FOR BLACK ROOK 
        if (x == 1) and (Movement.boardArr[x][y] in Piece.previousPiece) and (Movement.boardArr[x][y] == 'black'):
        
            # 2 steps forward valid 
            parseBoardToArray()
            x = x+1
            if (Movement.boardArr[x][y] == 'empty') or (Movement.boardArr[x][y] == Board.opposite(Board.play_belongs_to)):
                VALID_LIST.add((x,y))
                # Check the next step forward
                x = x+1
                # To avoid players first pawn move jumping over any piece or striking his own piece 
                if ((Movement.boardArr[x][y] == 'empty') and (Movement.boardArr[x-1][y] == 'empty')) or (Movement.boardArr[x][y] == Board.opposite(Board.play_belongs_to)):
                    if isPositionValidInArray((x, y)):
                        VALID_LIST.add((x,y))
            else:
                pass
            x,y = currentPosition


        elif (x != 1) and (Piece.previousPiece == 'blackPawn'):
            # 2 steps forward invalid only one 
            parseBoardToArray()
            x = x+1
            if (Movement.boardArr[x][y] == 'empty') or (Movement.boardArr[x][y] == Board.opposite(Board.play_belongs_to)):
                if isPositionValidInArray((x, y)):
                    VALID_LIST.add((x,y))
            else:
                pass
            x,y = currentPosition

        


        # Stop The main loop
        active = False

        # check player is not trying to move pawn backwards
        x,y = currentPosition
        if Board.play_belongs_to == 'white':
            # A white pawn cannot move backwards 
            for li in list(VALID_LIST):
            # check that every x cordinate is not increasing
            # if so remove the postion from valid_list
                if li[0] > x:
                    VALID_LIST.remove(li)
        elif Board.play_belongs_to == 'black':
            # A black pawn cannot move backwards 
            for li in list(VALID_LIST):
            # check that every x cordinate is not decreasing
            # if so remove the postion from valid_list
                if li[0] < x:
                    VALID_LIST.remove(li)

        print(f"\n\n Valid LIST : {VALID_LIST}")
        if destinationPosition in VALID_LIST:
            if (destinationPosition[0] == 0) or (destinationPosition[0] == 7):
                Board.pieces[Piece.position] = 'blackKnight'

            return True
        else:
            return False
            







    # return Movement.boardArr[0][0]

# def knight(currentPosition, futurePosition):
#     pass
# def bishop(currentPosition, futurePosition):
#     pass
# def queen(currentPosition, futurePosition):
#     pass
# def king(currentPosition, futurePosition):
#     pass

