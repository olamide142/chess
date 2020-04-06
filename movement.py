from board import Board
# from piece import Piece
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
                if Movement.boardArr[x][y] == 'empty':
                    VALID_LIST.append((x,y))
                elif Board.play_belongs_to not in Movement.boardArr[x][y]:
                    # if opponet player is along the valid path 
                    # allow the attacker to take him out
                    VALID_LIST.append((x,y))
                    left = False
            else:
                left = False
        x,y = currentPosition
            



        # Check all the boxes to the top of current position
        # and stops when there is a filled box
        while top:
            x -=1
            if isPositionValidInArray((x, y)):
                parseBoardToArray()
                if Movement.boardArr[x][y] == 'empty':
                    VALID_LIST.append((x,y))
                elif Board.play_belongs_to not in Movement.boardArr[x][y]:
                    # if opponet player is along the valid path 
                    # allow the attacker to take him out
                    VALID_LIST.append((x,y))
                    top = False
            else:
                top = False
        x,y = currentPosition
            

        
        # Check all the boxes to the right of current position
        # and stops when there is a filled box
        while right:
            y +=1
            if isPositionValidInArray((x, y)):
                parseBoardToArray()
                if Movement.boardArr[x][y] == 'empty':
                    VALID_LIST.append((x,y))
                elif Board.play_belongs_to not in Movement.boardArr[x][y]:
                    # if opponet player is along the valid path 
                    # allow the attacker to take him out
                    VALID_LIST.append((x,y))
                    right = False
            else:
                right = False
        x,y = currentPosition




        # Check all the boxes to the bottom of current position
        # and stops when there is a filled box
        while bottom:
            x +=1
            if isPositionValidInArray((x, y)):
                parseBoardToArray()
                if Movement.boardArr[x][y] == 'empty':
                    VALID_LIST.append((x,y))
                elif Board.play_belongs_to not in Movement.boardArr[x][y]:
                    # if opponet player is along the valid path 
                    # allow the attacker to take him out
                    VALID_LIST.append((x,y))
                    bottom = False
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





    # return Movement.boardArr[0][0]

# def knight(currentPosition, futurePosition):
#     pass
# def bishop(currentPosition, futurePosition):
#     pass
# def queen(currentPosition, futurePosition):
#     pass
# def king(currentPosition, futurePosition):
#     pass
# def pawn(currentPosition, futurePosition):
#     pass

