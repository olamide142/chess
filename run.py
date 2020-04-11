# from movement import *

# boardArr = [
#         ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
#         ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
#         ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
#         ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
#         ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
#         ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
#         ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
#         ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1'],
#     ]
    
# # list of positions that can be played to 
# valid_list = []

# def isPositionValidInArray(position):
#     """Returns True if such index exists in the array"""
#     # This is not a good approach 
#     # but it gets the job done
#     x = 0
#     y = 0
#     for i in Movement.A_copy:
#         if (x,y) == position:
#             return True
#         y += 1
#         if y > 7:
#             y = 0
#             x+=1
#     return False


# # Test algo
# currentPosition = (4,4)
# destinationPosition = (4,7)

# active = True

# left = True
# top = True
# right = True
# bottom = True

# while active:
#     x,y = currentPosition
#     # Check all the boxes to the left of current position
#     # and stops when there is a filled box
#     while left:
#         y -=1
#         if isPositionValidInArray((x, y)):
#             parseBoardToArray()
#             if Movement.boardArr[x][y] == 'empty':
#                 valid_list.append((x,y))
#             else:
#                 left = False
#         else:
#             left = False
#     x,y = currentPosition
        



#     # Check all the boxes to the top of current position
#     # and stops when there is a filled box
#     while top:
#         x -=1
#         if isPositionValidInArray((x, y)):
#             parseBoardToArray()
#             if Movement.boardArr[x][y] == 'empty':
#                 valid_list.append((x,y))
#             else:
#                 top = False
#         else:
#             top = False
#     x,y = currentPosition
        

    
#     # Check all the boxes to the right of current position
#     # and stops when there is a filled box
#     while right:
#         y +=1
#         if isPositionValidInArray((x, y)):
#             parseBoardToArray()
#             if Movement.boardArr[x][y] == 'empty':
#                 valid_list.append((x,y))
#             else:
#                 right = False
#         else:
#             right = False
#     x,y = currentPosition




#     # Check all the boxes to the bottom of current position
#     # and stops when there is a filled box
#     while bottom:
#         x +=1
#         if isPositionValidInArray((x, y)):
#             parseBoardToArray()
#             if Movement.boardArr[x][y] == 'empty':
#                 valid_list.append((x,y))
#             else:
#                 bottom = False
#         else:
#             bottom = False
#     x,y = currentPosition


#     # Stop The main loop
#     active = False
#     if destinationPosition in valid_list:
#         print(True)
#     else:
#         print(False)


# print(valid_list)
# print(Movement.pieces)

