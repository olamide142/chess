from player import Player 

class Board(Player):
    # Arrangement of all chess pieces
    pieces = {
        'A8':"blackRook", 'B8':"blackKnight", 'C8':"blackBishop", 'D8':"blackQueen", 'E8':"blackKing", 'F8':"blackBishop", 'G8':"blackKnight", 'H8':"blackRook",
        'A7':"blackPawn", 'B7':"blackPawn", 'C7':"blackPawn", 'D7':"blackPawn", 'E7':"blackPawn", 'F7':"blackPawn", 'G7':"blackPawn", 'H7':"blackPawn",
        'A6':"empty", 'B6':"empty", 'C6':"empty", 'D6':"empty", 'E6':"empty", 'F6':"empty", 'G6':"empty", 'H6':"empty",
        'A5':"empty", 'B5':"empty", 'C5':"empty", 'D5':"empty", 'E5':"empty", 'F5':"empty", 'G5':"empty", 'H5':"empty",
        'A4':"empty", 'B4':"empty", 'C4':"empty", 'D4':"empty", 'E4':"empty", 'F4':"empty", 'G4':"empty", 'H4':"empty",
        'A3':"empty", 'B3':"empty", 'C3':"empty", 'D3':"empty", 'E3':"empty", 'F3':"empty", 'G3':"empty", 'H3':"empty",
        'A2':"whiteQueen", 'B2':"whitePawn", 'C2':"whitePawn", 'D2':"whitePawn", 'E2':"whitePawn", 'F2':"whitePawn", 'G2':"whitePawn", 'H2':"whitePawn",
        'A1':"whiteRook", 'B1':"whiteKnight", 'C1':"whiteBishop", 'D1':"whiteQueen", 'E1':"whiteKing", 'F1':"whiteBishop", 'G1':"whiteKnight", 'H1':"whiteRook",
    }

    clone = pieces

    # This are the cordinates of each tile 
    # (left, top, right, bottom) same as graphical representation (-x, +y, +x, -y)
    locations = {
        'A8': (65, 64, 130, 129), 'B8': (130, 64, 195, 129), 'C8': (195, 64, 260, 129), 'D8': (260, 64, 325, 129), 'E8': (325, 64, 390, 129), 'F8': (390, 64, 455, 129), 'G8': (455, 64, 520, 129), 'H8': (520, 64, 585, 129), 
        'A7': (65, 128, 130, 193), 'B7': (130, 128, 195, 193), 'C7': (195, 128, 260, 193), 'D7': (260, 128, 325, 193), 'E7': (325, 128, 390, 193), 'F7': (390, 128, 455, 193), 'G7': (455, 128, 520, 193), 'H7': (520, 128, 585, 193), 
        'A6': (65, 192, 130, 257), 'B6': (130, 192, 195, 257), 'C6': (195, 192, 260, 257), 'D6': (260, 192, 325, 257), 'E6': (325, 192, 390, 257), 'F6': (390, 192, 455, 257), 'G6': (455, 192, 520, 257), 'H6': (520, 192, 585, 257), 
        'A5': (65, 256, 130, 321), 'B5': (130, 256, 195, 321), 'C5': (195, 256, 260, 321), 'D5': (260, 256, 325, 321), 'E5': (325, 256, 390, 321), 'F5': (390, 256, 455, 321), 'G5': (455, 256, 520, 321), 'H5': (520, 256, 585, 321), 
        'A4': (65, 320, 130, 385), 'B4': (130, 320, 195, 385), 'C4': (195, 320, 260, 385), 'D4': (260, 320, 325, 385), 'E4': (325, 320, 390, 385), 'F4': (390, 320, 455, 385), 'G4': (455, 320, 520, 385), 'H4': (520, 320, 585, 385), 
        'A3': (65, 384, 130, 449), 'B3': (130, 384, 195, 449), 'C3': (195, 384, 260, 449), 'D3': (260, 384, 325, 449), 'E3': (325, 384, 390, 449), 'F3': (390, 384, 455, 449), 'G3': (455, 384, 520, 449), 'H3': (520, 384, 585, 449), 
        'A2': (65, 448, 130, 513), 'B2': (130, 448, 195, 513), 'C2': (195, 448, 260, 513), 'D2': (260, 448, 325, 513), 'E2': (325, 448, 390, 513), 'F2': (390, 448, 455, 513), 'G2': (455, 448, 520, 513), 'H2': (520, 448, 585, 513), 
        'A1': (65, 512, 130, 577), 'B1': (130, 512, 195, 577), 'C1': (195, 512, 260, 577), 'D1': (260, 512, 325, 577), 'E1': (325, 512, 390, 577), 'F1': (390, 512, 455, 577), 'G1': (455, 512, 520, 577), 'H1': (520, 512, 585, 577)
        }

    # # list of pieces captured 
    # black = []
    # white = []

    # p = Player()
    # player = p.play_belongs_to 

    def __init__(self):
        # self.bg = pygame.image.load(os.path.join("sprites", "board.jpg"))
        pass

        
