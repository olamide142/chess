
class Player():
    play_belongs_to = 'white'


    def __init__(self):
        pass
        # Player.play_belongs_to = 'white'

    def switch_player():
        if Player.play_belongs_to == 'white':
            Player.play_belongs_to = 'black'
        else:
            Player.play_belongs_to = 'white'
    
    def opposite(color):
        if color == 'black':
            return 'white'
        elif color == 'white':
            return 'black'

