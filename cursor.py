import math
import random

class Cursor: 

    def __init__(self, window_width, window_height): 
        self.window_width = window_width
        self.window_height = window_height
        
        self.x = window_width // 2
        self.y =  window_height // 2

        self.cursor_speed = 5
        self.cursor_radius = 20
        
    def get_pos(self):
        return (self.x, self.y)

    # Defining cursor movement
    def move_cursor(self, target_x, target_y): 
        dx = self.x - target_x
        dy = self.y - target_y
        distance = math.hypot(dx, dy)

        if distance < 100:
            angle = math.atan2(dy, dx)
            angle += random.uniform(-0.15, 0.15) 
            self.x += self.cursor_speed * math.cos(angle)
            self.y += self.cursor_speed * math.sin(angle)

        self.clamp_to_window()
    
    # Force cursor to stay within the bounds of the window
    def clamp_to_window(self):
        self.x = max(self.cursor_radius, min(self.window_width - self.cursor_radius, self.x))
        self.y = max(self.cursor_radius, min(self.window_height - self.cursor_radius, self.y))

    # When cursor is caught, trigger method to spawn somewhere within the window
    def respawn_randomly(self): 
        self.x = random.randint(self.cursor_radius, self.window_width - self.cursor_radius)
        self.y = random.randint(self.cursor_radius, self.window_height - self.cursor_radius)