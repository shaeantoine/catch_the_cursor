import math
import pygame as pg
from cursor import Cursor 

class GameState: 
    
    # Initialize the game state
    def __init__(self, width, height):
        self.width = width
        self.height = height   
        self.font = pg.font.SysFont(None, 36)
        
        self.score = 0
        self.cursor = Cursor(window_width=width, window_height=height)

    def update(self):
        mx, my = pg.mouse.get_pos()
        self.cursor.move_cursor(mx, my)

        # Check if caught 
        dx = self.cursor.x - mx
        dy = self.cursor.y - my
        distance = math.hypot(dx, dy)
        if distance < self.cursor.cursor_radius:
            self.score += 1
            self.cursor.respawn_randomly()

    def draw(self, screen): 
        pg.draw.circle(screen, (200,50,50), self.cursor.get_pos(), self.cursor.cursor_radius)
        pg.draw.circle(screen, (255, 255, 255), self.cursor.get_pos(), 2)

        score_text = self.font.render(f"Score: {self.score}", True, (255,255,255))
        screen.blit(score_text, (10,10))
