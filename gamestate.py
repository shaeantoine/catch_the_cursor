from cursor import Cursor 

class GameState: 
    
    # Initialize the game state
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height 
        self.caption = caption        
        
        self.score = 0
        self.cursor = Cursor()

    def get_score(self):
        return self.score
    
    def increase_score(self):
        self.score += 1