

class Cursor: 

    def __init__(self): 
        self.cursor_speed = 5
        self.cursor_radius = 20
        self.cursor_pos = [self.width // 2, self.height // 2]

    def get_cursor_x(self):
        return self.cursor_pos[0] 
    
    def get_cursor_y(self):
        return self.cursor_pos[1]
    
    def set_cursor_x(self, new_x):
        self.cursor_pos[0] = new_x
    
    def set_cursor_x(self, new_y):
        self.cursor_pos[1] = new_y